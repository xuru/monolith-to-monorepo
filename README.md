# monolith-to-monorepo
Experimenting with moving a monolithic app to a monorepo

Development flow:

```shell
poetry install
docker-compose up -d
DATABASE_URL=postgres://root:root@localhost:5432/mtom-dev poetry run pytest
```

when ready to commit run:
```shell
poetry run pre-commit run
```
