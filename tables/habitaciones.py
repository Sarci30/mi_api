# tables/habitaciones.py
from flask import Blueprint, request, jsonify
from models import Habitacion, db

habitaciones_bp = Blueprint('habitaciones', __name__)

@habitaciones_bp.route('/habitaciones', methods=['GET'])
def get_habitaciones():
    habitaciones = Habitacion.query.all()
    return jsonify([{"id": h.id, "numero": h.numero, "tipo": h.tipo, "precio": h.precio} for h in habitaciones])

@habitaciones_bp.route('/habitaciones/<int:id>', methods=['GET'])
def get_habitacion(id):
    habitacion = Habitacion.query.get(id)
    if habitacion:
        return jsonify({"id": habitacion.id, "numero": habitacion.numero, "tipo": habitacion.tipo, "precio": habitacion.precio})
    return jsonify({"error": "Habitación no encontrada"}), 404

@habitaciones_bp.route('/habitaciones', methods=['POST'])
def add_habitacion():
    data = request.get_json()
    nueva_habitacion = Habitacion(numero=data['numero'], tipo=data['tipo'], precio=data['precio'])
    db.session.add(nueva_habitacion)
    db.session.commit()
    return jsonify({"message": "Habitación añadida"}), 201

@habitaciones_bp.route('/habitaciones/<int:id>', methods=['PUT'])
def update_habitacion(id):
    data = request.get_json()
    habitacion = Habitacion.query.get(id)
    if habitacion:
        habitacion.numero = data['numero']
        habitacion.tipo = data['tipo']
        habitacion.precio = data['precio']
        db.session.commit()
        return jsonify({"message": "Habitación actualizada"})
    return jsonify({"error": "Habitación no encontrada"}), 404

@habitaciones_bp.route('/habitaciones/<int:id>', methods=['DELETE'])
def delete_habitacion(id):
    habitacion = Habitacion.query.get(id)
    if habitacion:
        db.session.delete(habitacion)
        db.session.commit()
        return jsonify({"message": "Habitación eliminada"})
    return jsonify({"error": "Habitación no encontrada"}), 404
