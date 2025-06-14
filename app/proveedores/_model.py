from app.database import get_db_connection
import mysql.connector

class ProveedorModel:
    def __init__(self, id=None, nombre=None, telefono=None, direccion=None, email=None):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'email': self.email
        }

    @staticmethod
    def deserializar(data):
        return ProveedorModel(
            id=data.get('id'),
            nombre=data.get('nombre'),
            telefono=data.get('telefono'),
            direccion=data.get('direccion'),
            email=data.get('email')
        )

    @staticmethod
    def get_all():
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PROVEEDORES")
        proveedores = cursor.fetchall()
        cursor.close()
        cxn.close()
        return proveedores

    @staticmethod
    def get_one(id):
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PROVEEDORES WHERE id = %s", (id,))
        proveedor = cursor.fetchone()
        cursor.close()
        cxn.close()
        return proveedor

    def create(self):
        cxn = get_db_connection()
        if not cxn: return False
        cursor = cxn.cursor()
        query = "INSERT INTO PROVEEDORES (nombre, telefono, direccion, email) VALUES (%s, %s, %s, %s)"
        params = (self.nombre, self.telefono, self.direccion, self.email)
        try:
            cursor.execute(query, params)
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
        query = "UPDATE PROVEEDORES SET nombre=%s, telefono=%s, direccion=%s, email=%s WHERE id=%s"
        params = (self.nombre, self.telefono, self.direccion, self.email, self.id)
        try:
            cursor.execute(query, params)
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
            cursor.execute("DELETE FROM PROVEEDORES WHERE id = %s", (id,))
            cxn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            cxn.rollback()
            return False
        finally:
            cursor.close()
            cxn.close()