from app.database import get_db_connection
import mysql.connector
from ..marcas._model import MarcaModel
from ..proveedores._model import ProveedorModel
from ..categorias._model import CategoriaModel

class ArticuloModel:
    def __init__(self, id=None, descripcion=None, precio=None, stock=None, marca=None, proveedor=None, categorias=None):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca: MarcaModel = marca
        self.proveedor: ProveedorModel = proveedor
        self.categorias: list[CategoriaModel] = categorias if categorias is not None else []
        
    def serializar(self):
        return {
            'id': self.id,
            'descripcicion': self.descripcion,
            'precio': str(self.precio),
            'stock': self.stock,
            'marca': self.marca.serializar() if self.marca else None,
            'proveedor': self.proveedor.serializar() if self.proveedor else None,
            'categorias': [cat.serializar() for cat in self.categorias]
        }
        
    @staticmethod
    def deserializar(data):
        return ArticuloModel(
            id=data.get('id'),
            descripcion=data.get('descripcion'),
            precio=data.get('precio'),
            stock=data.get('stock'),
            marca=MarcaModel(id=data.get('proveedor_id')),
            proveedor=ProveedorModel(id=data.get('proveedor_id')),
            categorias=[CategoriaModel(id=cat_id) for cat_id in data.get('categorias_ids', [])]
        )
    
    @staticmethod
    def get_all():
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS")
        articulos_rows = cursor.fetchall()
        cursor.close()
        cxn.close()

        articulos = []
        if articulos_rows:
            for row in articulos_rows:
                marca_obj = MarcaModel.get_one(row['marca_id'])
                proveedor_obj = ProveedorModel.get_one(row['proveedor_id'])
                categorias_list = ArticuloModel._get_categorias_for_articulo(row['id'])

                articulo = ArticuloModel(
                    id=row['id'],
                    descripcion=row['descripcion'],
                    precio=row['precio'],
                    stock=row['stock'],
                    marca=MarcaModel.deserializar(marca_obj) if marca_obj else None,
                    proveedor=ProveedorModel.deserializar(proveedor_obj) if proveedor_obj else None,
                    categorias=categorias_list
                )
                articulos.append(articulo.serializar())
        return articulos
    
    @staticmethod
    def get_one(id):
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM ARTICULOS WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        cxn.close()
        
        if row:
            marca_obj = MarcaModel.get_one(row['marca_id'])
            proveedor_obj = ProveedorModel.get_one(row['proveedor_id'])
            categorias_list = ArticuloModel._get_categorias_for_articulo(row['id'])

            articulo = ArticuloModel(
                id=row['id'],
                descripcion=row['descripcion'],
                precio=row['precio'],
                stock=row['stock'],
                marca=MarcaModel.deserializar(marca_obj) if marca_obj else None,
                proveedor=ProveedorModel.deserializar(proveedor_obj) if proveedor_obj else None,
                categorias=categorias_list
            )
            return articulo.serializar()
        return None

    @staticmethod
    def _get_categorias_for_articulo(articulo_id):
        cxn = get_db_connection()
        if not cxn: return []
        cursor = cxn.cursor(dictionary=True)
        query = """
            SELECT c.id, c.nombre FROM CATEGORIAS c
            JOIN ARTICULOS_CATEGORIAS ac ON c.id = ac.categoria_id
            WHERE ac.articulo_id = %s
        """
        cursor.execute(query, (articulo_id,))
        cat_rows = cursor.fetchall()
        cursor.close()
        cxn.close()
        return [CategoriaModel.deserializar(cat) for cat in cat_rows]

    def create(self):
        cxn = get_db_connection()
        if not cxn: return None
        cursor = cxn.cursor()
        try:
            cxn.start_transaction()
            query_art = "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)"
            params_art = (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id)
            cursor.execute(query_art, params_art)
            self.id = cursor.lastrowid
            self._manage_categorias(cursor)

            cxn.commit()
            return self.id
        except mysql.connector.Error as err:
            cxn.rollback()
            print(f"Error al crear artículo: {err}")
            return None
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
            params_art = (self.descripcion, self.precio, self.stock, self.marca.id, self.proveedor.id, self.id)
            cursor.execute(query_art, params_art)

            self._manage_categorias(cursor)

            cxn.commit()
            return True
        except mysql.connector.Error as err:
            cxn.rollback()
            print(f"Error al actualizar artículo: {err}")
            return False
        finally:
            cursor.close()
            cxn.close()
    
    def _manage_categorias(self, cursor):
        cursor.execute("DELETE FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s", (self.id,))
        if self.categorias:
            query_cat = "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)"
            params_cat = [(self.id, cat.id) for cat in self.categorias]
            cursor.executemany(query_cat, params_cat)

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
            return False
        finally:
            cursor.close()
            cxn.close()