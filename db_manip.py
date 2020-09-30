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


def add_table(conn, cursor, table_name, cols_in_sql):
    command = 'CREATE TABLE {} '.format(table_name) + cols_in_sql
    cursor.execute(command)
    conn.commit()


def del_table(conn, cursor, table_name, truncate=False):
    command = 'TRUNCATE' if truncate else 'DROP'
    command += ' TABLE {}'.format(table_name)
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

    # see https://www.w3schools.com/sql/sql_primarykey.ASP

    cols_in_sql = '''(
        id INT NOT NULL,
        title VARCHAR(60),
        body TEXT,
        date DATETIME,
        img_path VARCHAR(60),
        url_to_link VARCHAR(60),
        PRIMARY KEY (id)
    )'''

    #add_table(conn, cursor, 'projects', cols_in_sql)
    #del_table(conn, cursor, 'projects')
    # Actually can just db.create_all() is better...

    conn.close()
