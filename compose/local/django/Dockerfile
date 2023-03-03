ARG PYTHON_VERSION=3.10.6-slim-bullseye
ARG APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1
ARG SHA_TAG
ARG APP_DIRECTORY=/app
ARG ARG_POETRY_VERSION=1.2.0

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

# Set configuration
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # wait script
    WAIT_VERSION=2.9.0 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=${ARG_POETRY_VERSION} \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    SETUP_PATH="/opt/setup"

ENV PATH=$POETRY_HOME/bin:$PATH


##############################################################################
# This stage is used to install dependencies and build the environment
##############################################################################
FROM python as python-build-stage

ARG BUILD_ENVIRONMENT=local

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
    zsh \
    curl \
    build-essential \
    libpq-dev \
    gettext \
    xmlsec1 \
    binutils \
    mime-support \
    procps \
    git \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libcairo2 \
    libpangocairo-1.0-0

WORKDIR ${SETUP_PATH}

# Now our python wheels
COPY ./poetry.lock* ./pyproject.toml ./
RUN pip install --upgrade pip setuptools \
    && curl -sSL https://install.python-poetry.org | python - \
    && ${POETRY_HOME}/bin/poetry export --with dev,test,lint -o requirements.txt --without-hashes \
    && pip wheel --wheel-dir ${SETUP_PATH}/wheels -r requirements.txt

# see: https://github.com/ufoscout/docker-compose-wait
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait


#################################################################################
# The 'run' stage
#################################################################################
FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=local
ARG APP_DIRECTORY=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_DIRECTORY}

RUN apt-get update && apt-get install -y  \
    build-essential \
    zsh \
    sudo \
    curl \
    libpq-dev \
    libyaml-dev \
    gettext \
    xmlsec1 \
    binutils \
    postgresql-client \
    mime-support \
    procps \
    supervisor \
    git \
    lsb-release \
    wget \
    zip \
    unzip \
    vim \
    openssl \
    tmux \
    xclip \
    htop \
    netcat-openbsd \
    colordiff \
    redis-tools \
    nmap \
    dnsutils \
    less \
    inetutils-ping \
    inetutils-traceroute \
    net-tools \
    netcat-openbsd \
    bsdmainutils \
    fonts-powerline \
    toilet figlet cowsay fortune-mod fortunes-min \
    && mkdir -p /var/log/supervisor \
    && apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*

# Setup home directory and shell
COPY ./compose/local/files/motd /etc/motd

ENV USER=mtom
ENV HOME=/home/$USER
ENV PATH=$PATH:$HOME/.local/bin
RUN groupadd -g 1000 $USER && useradd -u 1000 -g $USER -G sudo -m -s /usr/bin/zsh $USER && \
    sed -i /etc/sudoers -re 's/^%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^root.*/root ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^#includedir.*/## **Removed the include directive** ##"/g' && \
    echo "${USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    chmod +x /etc/motd && chsh -s /usr/bin/zsh mtom

# All absolute dir copies ignore workdir instruction. All relative dir copies are wrt to the workdir instruction
# copy python dependency wheels from python-build-stage
COPY --chown=mtom:mtom --from=python-build-stage ${SETUP_PATH}/wheels  /wheels/
COPY --chown=mtom:mtom --from=python-build-stage ${POETRY_HOME} ${POETRY_HOME}/
COPY --chown=mtom:mtom --from=python-build-stage /wait /wait

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && pip install superfsmon \
    && rm -rf /wheels

# Setup the mtom user shell
WORKDIR /home/mtom
COPY --chown=mtom ./compose/local/files/zshrc /home/mtom/.zshrc
RUN curl -sSL "https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh" | bash -s --  --keep-zshrc --skip-chsh \
    && chown -R mtom:mtom /home/mtom/.oh-my-zsh

RUN mkdir -p /var/log/mtom && chown -R mtom:mtom /var/log/mtom
USER mtom

# Will become mountpoint of our code
WORKDIR $APP_DIRECTORY

EXPOSE 8000
ENTRYPOINT ["/entrypoint"]
