from app.database import get_db_connection
import mysql.connector

class ArticuloModel:
    def __init__(self, id=None, descripcion=None, precio=None, stock=None, marca_id=None, proveedor_id=None, categoria_ids=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca_id = marca_id
        self.proveedor_id = proveedor_id
        self.categoria_ids = categoria_ids if categoria_ids is not None else []

    def serializar(self):
        # Este método no se usa directamente para la respuesta final,
        # ya que get_one construye el objeto completo.
        # Lo mantenemos por consistencia.
        return {
            'id': self.id, 'descripcion': self.descripcion, 'precio': str(self.precio),
            'stock': self.stock, 'marca_id': self.marca_id,
            'proveedor_id': self.proveedor_id, 'categoria_ids': self.categoria_ids
        }

    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data.get('id'),
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            stock=data.get('stock'),
            marca_id=data.get('marca_id'),
            proveedor_id=data.get('proveedor_id'),
            categoria_ids=data.get('categoria_ids', [])
        )

    @staticmethod
    def _fetch_related_data(articulo_row, cxn):
        """Función auxiliar para obtener los datos relacionados de un artículo."""
        cursor = cxn.cursor(dictionary=True)
        
        # Obtener marca
        cursor.execute("SELECT id, nombre FROM MARCAS WHERE id = %s", (articulo_row['marca_id'],))
        marca = cursor.fetchone()
        
        # Obtener proveedor
        cursor.execute("SELECT * FROM PROVEEDORES WHERE id = %s", (articulo_row['proveedor_id'],))
        proveedor = cursor.fetchone()
        
        # Obtener categorías
        query_cat = """
            SELECT c.id, c.nombre FROM CATEGORIAS c
            JOIN ARTICULOS_CATEGORIAS ac ON c.id = ac.categoria_id
            WHERE ac.articulo_id = %s
        """
        cursor.execute(query_cat, (articulo_row['id'],))
        categorias = cursor.fetchall()
        
        cursor.close()
        
        return {
            "id": articulo_row['id'],
            "descripcion": articulo_row['descripcion'],
            "precio": str(articulo_row['precio']),
            "stock": articulo_row['stock'],
            "marca": marca,
            "proveedor": proveedor,
            "categorias": categorias
        }

    @staticmethod
    def get_all():
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS")
        articulos_rows = cursor.fetchall()
        
        articulos_completos = []
        if articulos_rows:
            for row in articulos_rows:
                articulos_completos.append(ArticuloModel._fetch_related_data(row, cxn))

        cursor.close()
        cxn.close()
        return articulos_completos

    @staticmethod
    def get_one(id):
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS WHERE id = %s", (id,))
        articulo_row = cursor.fetchone()
        
        articulo_completo = None
        if articulo_row:
            articulo_completo = ArticuloModel._fetch_related_data(articulo_row, cxn)

        cursor.close()
        cxn.close()
        return articulo_completo

    def create(self):
        cxn = get_db_connection()
        if not cxn: return False
        cursor = cxn.cursor()
        try:
            cxn.start_transaction()
            query_art = "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)"
            params_art = (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id)
            cursor.execute(query_art, params_art)
            self.id = cursor.lastrowid
            
            if self.categoria_ids:
                query_cat = "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)"
                params_cat = [(self.id, cat_id) for cat_id in self.categoria_ids]
                cursor.executemany(query_cat, params_cat)
            
            cxn.commit()
            return True
        except mysql.connector.Error as err:
            cxn.rollback()
            print(f"Error al crear artículo: {err}")
            return False
        finally:
            cursor.close()
            cxn.close()

    def update(self):
        cxn = get_db_connection()
        if not cxn: return False
        cursor = cxn.cursor()
        try:
            cxn.start_transaction()
            query_art = "UPDATE ARTICULOS SET descripcion=%s, precio=%s, stock=%s, marca_id=%s, proveedor_id=%s WHERE id=%s"
            params_art = (self.descripcion, self.precio, self.stock, self.marca_id, self.proveedor_id, self.id)
            cursor.execute(query_art, params_art)

            cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (self.id,))
            if self.categoria_ids:
                query_cat = "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)"
                params_cat = [(self.id, cat_id) for cat_id in self.categoria_ids]
                cursor.executemany(query_cat, params_cat)

            cxn.commit()
            return True
        except mysql.connector.Error as err:
            cxn.rollback()
            print(f"Error al actualizar artículo: {err}")
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
            cxn.start_transaction()
            cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (id,))
            cursor.execute("DELETE FROM ARTICULOS WHERE id = %s", (id,))
            cxn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            cxn.rollback()
            print(f"Error al eliminar artículo: {err}")
            return False
        finally:
            cursor.close()
            cxn.close()