from database.connection import get_connection

def execute_query(query, parameters=()):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        connection.commit()
        return cursor
    finally:
        connection.close()

def fetch_one(query, parameters=()):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        return cursor.fetchone()
    finally:
        connection.close()

def fetch_all(query, parameters=()):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query, parameters)
        return cursor.fetchall()
    finally:
        connection.close()