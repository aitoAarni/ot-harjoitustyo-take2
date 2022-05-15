import sqlite3
from config import DATABASE_FILENAME_PATH


def get_database_connection():
    """establishes a connection to the database

    Returns:
        sqlite3.connect: connection object
    """
    connection = sqlite3.connect(DATABASE_FILENAME_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def drop_tables(con):
    """clears all the database of its contents

    Args:
        con (sqlite3.connect): connection to the database
    """
    cursor = con.cursor()

    cursor.execute(
        '''drop table if exists stats;'''
    )
    con.commit()


def create_tables(con):
    """Create the necessary rows to the table in the database

    Args:
        con (sqlite3.connect): connection to the database
    """
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE stats (id INTEGER PRIMARY KEY,
                            name TEXT UNIQUE,
                            attempts INTEGER,
                            wins INTEGER);
    ''')
    con.commit()


def initialize_database():
    """Deletes databse datble and creates a new one
    """
    conn = get_database_connection()
    drop_tables(conn)
    create_tables(conn)
