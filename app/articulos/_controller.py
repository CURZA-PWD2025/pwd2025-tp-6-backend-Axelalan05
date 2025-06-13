from ._model import ArticuloModel

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
        required = ['descripcion', 'precio', 'stock', 'marca_id', 'proveedor_id']
        if not all(field in data for field in required):
            return {"error": "Faltan campos requeridos"}, 400
        
        articulo = ArticuloModel.deserializar(data)
        if articulo.create():
            return ArticuloModel.get_one(articulo.id), 201
        return {"error": "No se pudo crear el artículo"}, 500

    @staticmethod
    def update(id, data):
        if not ArticuloModel.get_one(id):
            return {"error": "Artículo no encontrado"}, 404

        data['id'] = id
        articulo = ArticuloModel.deserializar(data)
        if articulo.update():
            # Devolvemos el objeto completo actualizado
            return ArticuloModel.get_one(id), 200
        return {"error": "No se pudo actualizar el artículo"}, 500

    @staticmethod
    def delete(id):
        if not ArticuloModel.get_one(id):
            return {"error": "Artículo no encontrado"}, 404
        
        if ArticuloModel.delete(id):
            return {"message": "Artículo eliminado exitosamente"}, 200
        return {"error": "No se pudo eliminar el artículo"}, 500