from app.database import get_db_connection
import mysql.connector

class MarcaModel:
    def __init__(self, id=None, nombre=None):
      self.id = id
      self.nombre = nombre
      
    def serializar(self):
        return{'id': self.id, 'nombre': self.nombre}
    
    @staticmethod
    def deserializar(data):
        return MarcaModel(id=data.get('id'), nombre=data.get('nombre'))
    
    @staticmethod
    def get_all():
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM MARCAS")
        marcas = cursor.fetchall()
        cursor.close()
        cxn.close()
        return marcas
    
    @staticmethod
    def get_one(id):
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM MARCAS WHERE id = %s", (id,))
        marca = cursor.fetchone()
        cursor.close()
        cxn.close()
        return marca
    
    def create(self):
        cxn = get_db_connection()
        if not cxn: return False
        cursor = cxn.cursor()
        try:
            cursor.execute("INSERT INTO MARCAS (nombre) VALUES (%)", (self.nombre,))
            cxn.commit()
            self.id = cursor.lastrowid
            return True
        except mysql.connector.Error as err:
            cxn.rollback()
            print(f"Error al crear marca: {err}")
            return False
        finally:
            cursor.close()
            cxn.close()
    
    def update(self):
        cxn = get_db_connection()
        if not cxn: return False
        cursor = cxn.cursor()
        try:
            cursor.execute("UPDATE MARCAS SET nombre = %s WHERE id = %s", (self.nombre, self.id))
            cxn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            cxn.rollback()
            print(f"Error al actualizar marca: {err}")
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
            cursor.execute("DELETE FROM MARCAS WHERE id = %s", (id,))
            cxn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            cxn.rollback()
            print(f"Error al eliminar marca: {err}")
            return False
        finally:
            cursor.close()
            cxn.close()
            