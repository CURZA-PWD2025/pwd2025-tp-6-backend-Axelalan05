from ._model import CategoriaModel

class CategoriaController:
    @staticmethod
    def get_all():
        categorias = CategoriaModel.get_all()
        return [cat for cat in categorias], 200

    @staticmethod
    def get_one(id):
        categoria = CategoriaModel.get_one(id)
        if categoria:
            return categoria, 200
        return {"error": "Categoría no encontrada"}, 404

    @staticmethod
    def create(data):
        if 'nombre' not in data:
            return {"error": "El campo 'nombre' es requerido"}, 400
        
        categoria = CategoriaModel.deserializar(data)
        if categoria.create():
            return categoria.serializar(), 201
        return {"error": "No se pudo crear la categoría"}, 500

    @staticmethod
    def update(id, data):
        if 'nombre' not in data:
            return {"error": "El campo 'nombre' es requerido"}, 400

        if not CategoriaModel.get_one(id):
            return {"error": "Categoría no encontrada"}, 404

        data['id'] = id
        categoria = CategoriaModel.deserializar(data)
        if categoria.update():
            return categoria.serializar(), 200
        return {"error": "No se pudo actualizar la categoría"}, 500

    @staticmethod
    def delete(id):
        if not CategoriaModel.get_one(id):
            return {"error": "Categoría no encontrada"}, 404
        
        if CategoriaModel.delete(id):
            return {"message": "Categoría eliminada exitosamente"}, 200
        return {"error": "No se pudo eliminar la categoría"}, 500