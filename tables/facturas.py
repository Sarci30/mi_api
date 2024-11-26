# tables/facturas.py
from flask import Blueprint, request, jsonify
from models import Factura, db

facturas_bp = Blueprint('facturas', __name__)

@facturas_bp.route('/facturas', methods=['GET'])
def get_facturas():
    facturas = Factura.query.all()
    return jsonify([{"id": f.id, "cliente_id": f.cliente_id, "total": f.total, "fecha": f.fecha} for f in facturas])

@facturas_bp.route('/facturas/<int:id>', methods=['GET'])
def get_factura(id):
    factura = Factura.query.get(id)
    if factura:
        return jsonify({"id": factura.id, "cliente_id": factura.cliente_id, "total": factura.total, "fecha": factura.fecha})
    return jsonify({"error": "Factura no encontrada"}), 404

@facturas_bp.route('/facturas', methods=['POST'])
def add_factura():
    data = request.get_json()
    nueva_factura = Factura(cliente_id=data['cliente_id'], total=data['total'], fecha=data['fecha'])
    db.session.add(nueva_factura)
    db.session.commit()
    return jsonify({"message": "Factura añadida"}), 201

@facturas_bp.route('/facturas/<int:id>', methods=['PUT'])
def update_factura(id):
    data = request.get_json()
    factura = Factura.query.get(id)
    if factura:
        factura.cliente_id = data['cliente_id']
        factura.total = data['total']
        factura.fecha = data['fecha']
        db.session.commit()
        return jsonify({"message": "Factura actualizada"})
    return jsonify({"error": "Factura no encontrada"}), 404

@facturas_bp.route('/facturas/<int:id>', methods=['DELETE'])
def delete_factura(id):
    factura = Factura.query.get(id)
    if factura:
        db.session.delete(factura)
        db.session.commit()
        return jsonify({"message": "Factura eliminada"})
    return jsonify({"error": "Factura no encontrada"}), 404
