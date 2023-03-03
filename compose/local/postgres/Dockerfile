FROM postgres:11-alpine
MAINTAINER mtom <ops@mtom.us>

COPY --chown=postgres init-user-db.sh /docker-entrypoint-initdb.d/
RUN chown -R postgres. /docker-entrypoint-initdb.d/*
