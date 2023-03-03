ARG PYTHON_VERSION=3.10.6-slim-bullseye
ARG APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1
ARG SHA_TAG
ARG ARG_POETRY_VERSION=1.2.0

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python-build

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
    POETRY_NO_INTERACTION=1

##############################################################################
# This stage is used to install dependencies and build the environment
##############################################################################

ARG BUILD_ENVIRONMENT=production

# Install what is needed in the build stage
RUN apt-get update && apt-get install --no-install-recommends -y \
    zsh \
    curl \
    build-essential \
    libpq-dev \
    gettext \
    xmlsec1 \
    binutils \
    git \
    mime-support \
    procps \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libcairo2 \
    libpangocairo-1.0-0

# see: https://github.com/ufoscout/docker-compose-wait
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

# Install poetry
RUN pip install --upgrade pip setuptools \
    && curl -sSL https://install.python-poetry.org | python - \
    && ${POETRY_HOME}/bin/poetry config virtualenvs.in-project true

# Install virtual env
RUN mkdir /app
WORKDIR /app
COPY ./poetry.lock* ./pyproject.toml ./
RUN ${POETRY_HOME}/bin/poetry install --without test,lint,dev --no-root --no-interaction --no-ansi


#################################################################################
# The 'run' stage
#################################################################################
FROM python:${PYTHON_VERSION} as python-run-stage

ARG BUILD_ENVIRONMENT=production

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

RUN mkdir /app
WORKDIR /app

COPY --from=python-build /wait /wait
COPY --from=python-build /app/.venv/ /app/.venv
COPY . .

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    # psycopg2 dependencies
    libpq-dev \
    # Translations dependencies
    gettext \
    xmlsec1 \
    binutils \
    mime-support \
    procps \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libcairo2 \
    libpangocairo-1.0-0 \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*


RUN echo "export AWS_CONTAINER_CREDENTIALS_RELATIVE_URI=$AWS_CONTAINER_CREDENTIALS_RELATIVE_URI" >> /root/.profile && \
    mkdir -p /etc/security && \
    echo "*         hard    nofile      500000" >> /etc/security/limits.conf && \
    echo "*         soft    nofile      500000" >> /etc/security/limits.conf && \
    echo "root      hard    nofile      500000" >> /etc/security/limits.conf && \
    echo "root      soft    nofile      500000" >> /etc/security/limits.conf

COPY ./compose/production/django/entrypoint /entrypoint
COPY ./compose/production/django/start /start
COPY ./compose/production/django/migrate /start-migrate
COPY ./compose/production/django/celery/worker/start /start-celeryworker
COPY ./compose/production/django/celery/beat/start /start-celerybeat
RUN chmod +x /entrypoint
RUN chmod +x /start*

ENV SENTRY_RELEASE $SHA_TAG

# Explicitly put our code on PYTHONPATH to avoid having to install poetry and activiate it on this layer.
ENV PYTHONPATH=/app

# Make sure our virtualenv is used by default when we execute `python` in the container. This is the same as
# the `activate` magic, but done by hand. See https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV /app/.venv
ENV PATH "/app/.venv/bin:${PATH}"

RUN chmod 777 -R /app

VOLUME ["/app"]
EXPOSE 8000
ENTRYPOINT ["/entrypoint"]
