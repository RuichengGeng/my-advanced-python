## There are several useful tools in database management
- [sqlalchemy](https://www.sqlalchemy.org/), sqlalchemy is ORM(object-relational-mapping), [why ORM](https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a)
- [psycopg2](https://pypi.org/project/psycopg2/) , postgresql database adapter for python
- [alembic: database migrations tool](https://alembic.sqlalchemy.org/en/latest/), just some commands to key in cmd to change database ...but useful :)



** Good tutorials **
- [Get started with alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [Get started with sqlalchemy](https://docs.sqlalchemy.org/en/14/tutorial/index.html), main point is ORM and core
- [Get started with psycopg](https://www.psycopg.org/docs/index.html)
- [a YouTube Video](https://www.youtube.com/watch?v=nt5sSr1A_qw)

**Things to notice**
- Run all alembic command under database_management folder

**some useful alembic command, please run these command under data management folder!**
- alembic revision --autogenerate -m "Create user model"
- alembic upgrade head
- alembic downgrade -1


### Starting PostgreSQL container
It is recommended to develop against a PostgreSQL database server running locally in a docker container. Assuming you installed Docker(Docker desktop and before Docker,you should install WSL and Ubuntu), you can start such a container by for example running:
```
docker run -e POSTGRES_PASSWORD=ruicheng -e POSTGRES_USER=ruicheng -e PGDATA=/var/lib/postgresql/data/pgdata -v /var/lib/postgresql/data -p 5432:5432 --restart=unless-stopped --detach postgres:13.1
```
