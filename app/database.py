import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

load_dotenv()

db_pool = None
try:
    # Creamos un pool de conexiones para manejar las conexiones a la DB de forma eficiente
    db_pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="my_pool",
        pool_size=5,
        pool_reset_session=True,
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")
        # No agregues 'auth_plugin' a menos que el cambio de host a 127.0.0.1 no funcione
    )
    print("Pool de conexiones a la base de datos creado exitosamente.")

except mysql.connector.Error as err:
    print(f"Error al crear el pool de conexiones: {err}")
    # db_pool se quedará como None si falla la creación

def get_db_connection():
    """
    Obtiene una conexión del pool.
    Si el pool no está disponible, devuelve None.
    """
    if db_pool:
        try:
            # Pide una conexión al pool
            return db_pool.get_connection()
        except mysql.connector.Error as err:
            print(f"Error al obtener la conexión del pool: {err}")
            return None
    else:
        # Esto se ejecutará si el pool no se pudo crear al inicio
        print("El pool de conexiones no está disponible.")
        return None