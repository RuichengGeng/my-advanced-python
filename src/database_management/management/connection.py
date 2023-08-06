from typing import Callable, Iterable, TypeVar
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


from database_management.domain.database_config import DatabaseConfiguration

T = TypeVar("T")
_logger = logging.getLogger(__name__)


class Connection:
    def __init__(self, config: DatabaseConfiguration):
        self._config = config

        try:
            self._engine = self.create_db_engine()
            self._db_session = scoped_session(sessionmaker(bind=self._engine))
            _logger.info("Connecting database")
        except AttributeError as ae:
            print("Database session unavailable because: " + str(ae))

    def create_db_engine(self):
        return create_engine(
            self._config.connection_string + "/" + self._config.database,
            pool_recycle=3600,
            pool_pre_ping=True,
            # TODO: might need timeout config, just keep it here
            # connect_args={
            #     "options": f"-c statement_timeout={self._config.time_out_seconds}s "
            #     f"-c lock_timeout={self._config.time_out_seconds}s "
            #     f"-c idle_in_transaction_session_timeout={self._config.time_out_seconds}s"
            # },
        )

    def do(self, operation: Callable[[Session], T]) -> T:
        session: Session = self._db_session()
        try:
            return operation(session)
        except Exception as ex:
            session.rollback()
            raise ex
        finally:
            session.close()

    def do_with_engine(self, operation: Callable):
        connection = self._engine.connect()
        transaction = connection.begin()
        try:
            result = operation(connection, transaction)
            transaction.commit()
            return result
        except Exception as ex:
            transaction.rollback()
            raise ex
        finally:
            transaction.close()
            connection.close()

    def do_with_psycopg_cursor(self, operation: Callable):
        connection = self._engine.raw_connection()
        cursor = connection.cursor()
        try:
            result = operation(connection, cursor)
            connection.commit()
            return result
        except Exception as ex:
            raise ex
        finally:
            cursor.close()
            connection.close()

    def read_with_cursor(self, operation: Callable):
        connection = self._engine.raw_connection()
        cursor = connection.cursor()
        try:
            result = operation(cursor)
            return result
        except Exception as ex:
            raise ex
        finally:
            cursor.close()
            connection.close()

    def read_with_engine(self, operation: Callable):
        connection = self._engine.connect()
        try:
            result = operation(connection)
            return result
        except Exception as ex:
            raise ex
        finally:
            connection.close()

    def iterate_with_psycopg_cursor(self, operation: Callable) -> Iterable:
        connection = self._engine.raw_connection()
        # we have to provide a name to the cursor, otherwise the whole dataset will be
        # loaded into memory. this is not documented anywhere...
        # https://stackoverflow.com/questions/17199113/psycopg2-leaking-memory-after-large-query
        cursor = connection.cursor(name="my_cursor")
        try:
            yield from operation(connection, cursor)
        except Exception as ex:
            raise ex
        finally:
            cursor.close()
            connection.close()


class BaseRepository:
    def __init__(self, db_connection: Connection):
        # TODO: might need more than 1 database, can use a dict to store engine
        #  or just instantiate more than one base repo
        #  or use derived classes to do specific jobs
        self._db_connection = db_connection

    def do(self, operation: Callable[[Session], T]) -> T:
        return self._db_connection.do(operation)

    def do_with_engine(self, operation: Callable):
        return self._db_connection.do_with_engine(operation)

    def do_with_psycopg_cursor(self, operation: Callable):
        return self._db_connection.do_with_psycopg_cursor(operation)

    def iterate_with_psycopg_cursor(self, operation: Callable) -> Iterable:
        return self._db_connection.iterate_with_psycopg_cursor(operation)

    def read_with_cursor(self, operation: Callable):
        return self._db_connection.read_with_cursor(operation)

    def read_with_engine(self, operation: Callable):
        return self._db_connection.read_with_engine(operation)
