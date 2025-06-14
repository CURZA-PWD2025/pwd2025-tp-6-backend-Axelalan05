from flask import Blueprint, request, jsonify
from ._controller import ProveedorController

proveedores_bp = Blueprint('proveedores', __name__)

@proveedores_bp.route('/', methods=['GET'])
def get_proveedores():
    response, status = ProveedorController.get_all()
    return jsonify(response), status

@proveedores_bp.route('/<int:id>', methods=['GET'])
def get_proveedor(id):
    response, status = ProveedorController.get_one(id)
    return jsonify(response), status

@proveedores_bp.route('/', methods=['POST'])
def create_proveedor():
    data = request.get_json()
    response, status = ProveedorController.create(data)
    return jsonify(response), status

@proveedores_bp.route('/<int:id>', methods=['PUT'])
def update_proveedor(id):
    data = request.get_json()
    response, status = ProveedorController.update(id, data)
    return jsonify(response), status

@proveedores_bp.route('/<int:id>', methods=['DELETE'])
def delete_proveedor(id):
    response, status = ProveedorController.delete(id)
    return jsonify(response), status