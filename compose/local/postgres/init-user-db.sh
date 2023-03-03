#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER root WITH PASSWORD 'root' SUPERUSER CREATEDB;
    CREATE DATABASE mtom-dev;
    GRANT ALL PRIVILEGES ON DATABASE mtom-dev TO root;
EOSQL
