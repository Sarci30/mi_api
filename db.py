import mysql.connector
from mysql.connector import Error

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_clientes'
        )
    except Error as e:
        print(f"Error de conexión a la base de datos: {e}")
    return connection
