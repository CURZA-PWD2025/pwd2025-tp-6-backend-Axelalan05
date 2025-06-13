from ._model import ProveedorModel

class ProveedorController:
    @staticmethod
    def get_all():
        return ProveedorModel.get_all(), 200

    @staticmethod
    def get_one(id):
        proveedor = ProveedorModel.get_one(id)
        if proveedor:
            return proveedor, 200
        return {"error": "Proveedor no encontrado"}, 404

    @staticmethod
    def create(data):
        required_fields = ['nombre', 'telefono', 'direccion', 'email']
        if not all(field in data for field in required_fields):
            return {"error": "Faltan campos requeridos"}, 400
        
        proveedor = ProveedorModel.deserializar(data)
        if proveedor.create():
            return proveedor.serializar(), 201
        return {"error": "No se pudo crear el proveedor"}, 500

    @staticmethod
    def update(id, data):
        if not ProveedorModel.get_one(id):
            return {"error": "Proveedor no encontrado"}, 404
        
        data['id'] = id
        proveedor = ProveedorModel.deserializar(data)
        if proveedor.update():
            return proveedor.serializar(), 200
        return {"error": "No se pudo actualizar el proveedor"}, 500

    @staticmethod
    def delete(id):
        if not ProveedorModel.get_one(id):
            return {"error": "Proveedor no encontrado"}, 404
        
        if ProveedorModel.delete(id):
            return {"message": "Proveedor eliminado exitosamente"}, 200
        return {"error": "No se pudo eliminar el proveedor"}, 500