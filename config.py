# config.py
from flask_sqlalchemy import SQLAlchemy

# Aquí usamos la configuración local de MySQL en XAMPP
DATABASE_URI = "mysql+pymysql://root:@localhost/bd_cliente"  # 'root' es el usuario por defecto de XAMPP
db = SQLAlchemy()
