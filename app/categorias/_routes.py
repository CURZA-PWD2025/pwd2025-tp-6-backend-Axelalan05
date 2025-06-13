from flask import Blueprint, request, jsonify
from ._controller import CategoriaController

categorias_bp = Blueprint('categorias', __name__)

@categorias_bp.route('/', methods=['GET'])
def get_categorias():
    response, status = CategoriaController.get_all()
    return jsonify(response), status

@categorias_bp.route('/<int:id>', methods=['GET'])
def get_categoria(id):
    response, status = CategoriaController.get_one(id)
    return jsonify(response), status

@categorias_bp.route('/', methods=['POST'])
def create_categoria():
    data = request.get_json()
    response, status = CategoriaController.create(data)
    return jsonify(response), status

@categorias_bp.route('/<int:id>', methods=['PUT'])
def update_categoria(id):
    data = request.get_json()
    response, status = CategoriaController.update(id, data)
    return jsonify(response), status

@categorias_bp.route('/<int:id>', methods=['DELETE'])
def delete_categoria(id):
    response, status = CategoriaController.delete(id)
    return jsonify(response), status