import sqlite3
from config import DATABASE_FILENAME_PATH


def get_database_connection():

    connection = sqlite3.connect(DATABASE_FILENAME_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def drop_tables(con):
    cursor = con.cursor()

    cursor.execute(
        '''drop table if exists stats;'''
    )
    con.commit()


def create_tables(con):
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE stats (id INTEGER PRIMARY KEY,
                            name TEXT UNIQUE,
                            attempts INTEGER,
                            wins INTEGER);
    ''')
    con.commit()


def initialize_database():
    conn = get_database_connection()
    drop_tables(conn)
    create_tables(conn)
