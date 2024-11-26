# models.py
from config import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefono = db.Column(db.String(20))

class Habitacion(db.Model):
    __tablename__ = 'habitaciones'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False, unique=True)
    tipo = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    habitacion_id = db.Column(db.Integer, db.ForeignKey('habitaciones.id'), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    cliente = db.relationship('Cliente', backref='reservas')
    habitacion = db.relationship('Habitacion', backref='reservas')

class Servicio(db.Model):
    __tablename__ = 'servicios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))

class Factura(db.Model):
    __tablename__ = 'facturas'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    cliente = db.relationship('Cliente', backref='facturas')

class Pago(db.Model):
    __tablename__ = 'pagos'
    id = db.Column(db.Integer, primary_key=True)
    factura_id = db.Column(db.Integer, db.ForeignKey('facturas.id'), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    factura = db.relationship('Factura', backref='pagos')

class Empleado(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamentos.id'), nullable=False)
    departamento = db.relationship('Departamento', backref='empleados')

class Departamento(db.Model):
    __tablename__ = 'departamentos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))

class Inventario(db.Model):
    __tablename__ = 'inventario'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'))
    proveedor = db.relationship('Proveedor', backref='inventario')

class Mantenimiento(db.Model):
    __tablename__ = 'mantenimiento'
    id = db.Column(db.Integer, primary_key=True)
    habitacion_id = db.Column(db.Integer, db.ForeignKey('habitaciones.id'))
    descripcion = db.Column(db.String(255))
    fecha = db.Column(db.Date)
    habitacion = db.relationship('Habitacion', backref='mantenimiento')
