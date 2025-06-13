from flask import Blueprint, request, jsonify
from ._controller import ArticuloController

articulos_bp = Blueprint('articulos', __name__)

@articulos_bp.route('/', methods=['GET'])
def get_articulos():
    response, status = ArticuloController.get_all()
    return jsonify(response), status

@articulos_bp.route('/<int:id>', methods=['GET'])
def get_articulo(id):
    response, status = ArticuloController.get_one(id)
    return jsonify(response), status

@articulos_bp.route('/', methods=['POST'])
def create_articulo():
    data = request.get_json()
    response, status = ArticuloController.create(data)
    return jsonify(response), status

@articulos_bp.route('/<int:id>', methods=['PUT'])
def update_articulo(id):
    data = request.get_json()
    response, status = ArticuloController.update(id, data)
    return jsonify(response), status

@articulos_bp.route('/<int:id>', methods=['DELETE'])
def delete_articulo(id):
    response, status = ArticuloController.delete(id)
    return jsonify(response), status