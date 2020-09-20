import sqlite3
import pandas as pd


def get_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cursor.fetchall()


def print_table(conn, table):
    query = 'SELECT * FROM {}'.format(table)  # Note not sql injection secure
    df = pd.read_sql_query(query, conn)

    print('\nPrinting table {}'.format(table))
    print(df)


def add_column(conn, cursor, table, column, data_type):
    command = 'ALTER TABLE {} ADD column {} {}'.format(
                                                table, column, data_type)
    cursor.execute(command)
    conn.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('website_data.db')
    cursor = conn.cursor()

    tables = get_tables(cursor)

    for table in tables:
        print_table(conn, table[0])

    #add_column(conn, cursor, 'user', 'about_me', 'VARCHAR(140)')
    #add_column(conn, cursor, 'user', 'last_seen', 'DATETIME')
    conn.close()

