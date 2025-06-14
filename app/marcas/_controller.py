from ._model import MarcaModel

class MarcaController:
    @staticmethod
    def get_all():
        marcas = MarcaModel.get_all()
        return [marca for marca in marcas], 200

    @staticmethod
    def get_one(id):
        marca = MarcaModel.get_one(id)
        if marca:
            return marca, 200
        return {"error": "Marca no encontrada"}, 404

    @staticmethod
    def create(data):
        if 'nombre' not in data:
            return {"error": "El campo 'nombre' es requerido"}, 400
        
        marca = MarcaModel.deserializar(data)
        if marca.create():
            return marca.serializar(), 201
        return {"error": "No se pudo crear la marca"}, 500

    @staticmethod
    def update(id, data):
        if 'nombre' not in data:
            return {"error": "El campo 'nombre' es requerido"}, 400

        if not MarcaModel.get_one(id):
            return {"error": "Marca no encontrada"}, 404

        data['id'] = id
        marca = MarcaModel.deserializar(data)
        if marca.update():
            return marca.serializar(), 200
        return {"error": "No se pudo actualizar la marca"}, 500

    @staticmethod
    def delete(id):
        if not MarcaModel.get_one(id):
            return {"error": "Marca no encontrada"}, 404
        
        if MarcaModel.delete(id):
            return {"message": "Marca eliminada exitosamente"}, 200
        return {"error": "No se pudo eliminar la marca"}, 500