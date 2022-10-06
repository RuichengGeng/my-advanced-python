## Alembic a very easy and useful tool to do database management, including nealy all operations
- [Get started with tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [a YouTube Video](https://www.youtube.com/watch?v=nt5sSr1A_qw)  
  
## Things to notice
- Run all alembic command under database_management folder

## some useful alembic command, please run these command under data management folder!
- alembic revision --autogenerate -m "Create user model"
- alembic upgrade head
- alembic downgrade -1