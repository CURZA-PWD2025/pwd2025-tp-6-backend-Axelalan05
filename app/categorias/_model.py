from app.database import get_db_connection
import mysql.connector

class CategoriaModel:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {'id': self.id, 'nombre': self.nombre}

    @staticmethod
    def deserializar(data):
        return CategoriaModel(id=data.get('id'), nombre=data.get('nombre'))

    @staticmethod
    def get_all():
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM CATEGORIAS")
        categorias = cursor.fetchall()
        cursor.close()
        cxn.close()
        return categorias

    @staticmethod
    def get_one(id):
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM CATEGORIAS WHERE id = %s", (id,))
        categoria = cursor.fetchone()
        cursor.close()
        cxn.close()
        return categoria

    def create(self):
        cxn = get_db_connection()
        if not cxn: return False
        cursor = cxn.cursor()
        try:
            cursor.execute("INSERT INTO CATEGORIAS (nombre) VALUES (%s)", (self.nombre,))
            cxn.commit()
            self.id = cursor.lastrowid
            return True
        except mysql.connector.Error as err:
            cxn.rollback()
            return False
        finally:
            cursor.close()
            cxn.close()

    def update(self):
        cxn = get_db_connection()
        if not cxn: return False
        cursor = cxn.cursor()
        try:
            cursor.execute("UPDATE CATEGORIAS SET nombre = %s WHERE id = %s", (self.nombre, self.id))
            cxn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            cxn.rollback()
            return False
        finally:
            cursor.close()
            cxn.close()

    @staticmethod
    def delete(id):
        cxn = get_db_connection()
        if not cxn: return False
        cursor = cxn.cursor()
        try:
            cursor.execute("DELETE FROM CATEGORIAS WHERE id = %s", (id,))
            cxn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            cxn.rollback()
            return False
        finally:
            cursor.close()
            cxn.close()