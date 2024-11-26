# tables/reservas.py
from flask import Blueprint, request, jsonify
from models import Reserva, db

reservas_bp = Blueprint('reservas', __name__)

@reservas_bp.route('/reservas', methods=['GET'])
def get_reservas():
    reservas = Reserva.query.all()
    return jsonify([{"id": r.id, "cliente_id": r.cliente_id, "habitacion_id": r.habitacion_id, "fecha_inicio": r.fecha_inicio, "fecha_fin": r.fecha_fin} for r in reservas])

@reservas_bp.route('/reservas/<int:id>', methods=['GET'])
def get_reserva(id):
    reserva = Reserva.query.get(id)
    if reserva:
        return jsonify({"id": reserva.id, "cliente_id": reserva.cliente_id, "habitacion_id": reserva.habitacion_id, "fecha_inicio": reserva.fecha_inicio, "fecha_fin": reserva.fecha_fin})
    return jsonify({"error": "Reserva no encontrada"}), 404

@reservas_bp.route('/reservas', methods=['POST'])
def add_reserva():
    data = request.get_json()
    nueva_reserva = Reserva(cliente_id=data['cliente_id'], habitacion_id=data['habitacion_id'], fecha_inicio=data['fecha_inicio'], fecha_fin=data['fecha_fin'])
    db.session.add(nueva_reserva)
    db.session.commit()
    return jsonify({"message": "Reserva añadida"}), 201

@reservas_bp.route('/reservas/<int:id>', methods=['PUT'])
def update_reserva(id):
    data = request.get_json()
    reserva = Reserva.query.get(id)
    if reserva:
        reserva.cliente_id = data['cliente_id']
        reserva.habitacion_id = data['habitacion_id']
        reserva.fecha_inicio = data['fecha_inicio']
        reserva.fecha_fin = data['fecha_fin']
        db.session.commit()
        return jsonify({"message": "Reserva actualizada"})
    return jsonify({"error": "Reserva no encontrada"}), 404

@reservas_bp.route('/reservas/<int:id>', methods=['DELETE'])
def delete_reserva(id):
    reserva = Reserva.query.get(id)
    if reserva:
        db.session.delete(reserva)
        db.session.commit()
        return jsonify({"message": "Reserva eliminada"})
    return jsonify({"error": "Reserva no encontrada"}), 404
