from ._model import ArticuloModel
from ..marcas._model import MarcaModel
from ..proveedores._model import ProveedorModel
from ..categorias._model import CategoriaModel

class ArticuloController:
    @staticmethod
    def get_all():
        articulos = ArticuloModel.get_all()
        return articulos, 200

    @staticmethod
    def get_one(id):
        articulo = ArticuloModel.get_one(id)
        if articulo:
            return articulo, 200
        return {"error": "Artículo no encontrado"}, 404

    @staticmethod
    def create(data):
        try:
            required = ['descripcion', 'precio', 'stock', 'marca_id', 'proveedor_id']
            if not all(field in data for field in required):
                return {"error": "Faltan campos requeridos"}, 400

            marca = MarcaModel(id=data['marca_id'])
            proveedor = ProveedorModel(id=data['proveedor_id'])
            categorias = [CategoriaModel(id=cat_id) for cat_id in data.get('categoria_ids', [])]
            
            articulo = ArticuloModel(
                descripcion=data['descripcion'],
                precio=data['precio'],
                stock=data['stock'],
                marca=marca,
                proveedor=proveedor,
                categorias=categorias
            )
            
            new_id = articulo.create()
            if new_id:
                return ArticuloModel.get_one(new_id), 201
            
            return {"error": "No se pudo crear el artículo"}, 500
        except Exception as e:
            return {"error": f"Ocurrió un error: {e}"}, 500

    @staticmethod
    def update(id, data):
        try:
            if not ArticuloModel.get_one(id):
                return {"error": "Artículo no encontrado"}, 404

            marca = MarcaModel(id=data['marca_id'])
            proveedor = ProveedorModel(id=data['proveedor_id'])
            categorias = [CategoriaModel(id=cat_id) for cat_id in data.get('categoria_ids', [])]

            articulo = ArticuloModel(
                id=id,
                descripcion=data['descripcion'],
                precio=data['precio'],
                stock=data['stock'],
                marca=marca,
                proveedor=proveedor,
                categorias=categorias
            )

            if articulo.update():
                return ArticuloModel.get_one(id), 200
            
            return {"error": "No se pudo actualizar el artículo"}, 500
        except Exception as e:
            return {"error": f"Ocurrió un error: {e}"}, 500


    @staticmethod
    def delete(id):
        if not ArticuloModel.get_one(id):
            return {"error": "Artículo no encontrado"}, 404
        
        if ArticuloModel.delete(id):
            return {"message": "Artículo eliminado exitosamente"}, 200
        return {"error": "No se pudo eliminar el artículo"}, 500