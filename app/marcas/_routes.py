from flask import Blueprint, request, jsonify
from ._controller import MarcaController

marcas_bp = Blueprint('marcas', __name__)

@marcas_bp.route('/', methods=['GET'])
def get_marcas():
    response, status = MarcaController.get_all()
    return jsonify(response), status

@marcas_bp.route('/<int:id>', methods=['GET'])
def get_marca(id):
    response, status = MarcaController.get_one(id)
    return jsonify(response), status

@marcas_bp.route('/', methods=['POST'])
def create_marca():
    data = request.get_json()
    response, status = MarcaController.create(data)
    return jsonify(response), status

@marcas_bp.route('/<int:id>', methods=['PUT'])
def update_marca(id):
    data = request.get_json()
    response, status = MarcaController.update(id, data)
    return jsonify(response), status

@marcas_bp.route('/<int:id>', methods=['DELETE'])
def delete_marca(id):
    response, status = MarcaController.delete(id)
    return jsonify(response), status