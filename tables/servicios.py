# tables/servicios.py
from flask import Blueprint, request, jsonify
from models import Servicio, db

servicios_bp = Blueprint('servicios', __name__)

@servicios_bp.route('/servicios', methods=['GET'])
def get_servicios():
    servicios = Servicio.query.all()
    return jsonify([{"id": s.id, "nombre": s.nombre, "descripcion": s.descripcion} for s in servicios])

@servicios_bp.route('/servicios/<int:id>', methods=['GET'])
def get_servicio(id):
    servicio = Servicio.query.get(id)
    if servicio:
        return jsonify({"id": servicio.id, "nombre": servicio.nombre, "descripcion": servicio.descripcion})
    return jsonify({"error": "Servicio no encontrado"}), 404

@servicios_bp.route('/servicios', methods=['POST'])
def add_servicio():
    data = request.get_json()
    nuevo_servicio = Servicio(nombre=data['nombre'], descripcion=data.get('descripcion'))
    db.session.add(nuevo_servicio)
    db.session.commit()
    return jsonify({"message": "Servicio añadido"}), 201

@servicios_bp.route('/servicios/<int:id>', methods=['PUT'])
def update_servicio(id):
    data = request.get_json()
    servicio = Servicio.query.get(id)
    if servicio:
        servicio.nombre = data['nombre']
        servicio.descripcion = data.get('descripcion')
        db.session.commit()
        return jsonify({"message": "Servicio actualizado"})
    return jsonify({"error": "Servicio no encontrado"}), 404

@servicios_bp.route('/servicios/<int:id>', methods=['DELETE'])
def delete_servicio(id):
    servicio = Servicio.query.get(id)
    if servicio:
        db.session.delete(servicio)
        db.session.commit()
        return jsonify({"message": "Servicio eliminado"})
    return jsonify({"error": "Servicio no encontrado"}), 404
