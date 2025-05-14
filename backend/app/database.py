import pymysql.cursors
from contextlib import contextmanager
from .config import settings

@contextmanager
def get_db():
    connection = pymysql.connect(
        host=settings.DB_HOST,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
    try:
        yield connection
    finally:
        connection.close()