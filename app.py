from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import text

app = Flask(__name__)
CORS(app)  # Esto habilita CORS para todas las rutas

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://uvp:rojito33@20.151.93.235/bd_cliente'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/api/tables', methods=['GET'])
def get_tables():
    try:
        # Ejecuta la consulta 'SHOW TABLES' para obtener las tablas
        result = db.session.execute(text("SHOW TABLES"))
        tables = [row[0] for row in result]  # Extrae los nombres de las tablas
        return jsonify(tables), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/tables/<table_name>', methods=['GET'])
def get_table_data(table_name):
    try:
        # Verifica que la tabla existe en la base de datos
        tables = db.session.execute(text("SHOW TABLES")).fetchall()
        table_names = [row[0] for row in tables]

        if table_name not in table_names:
            return jsonify({"error": f"La tabla '{table_name}' no existe en la base de datos."}), 404

        # Obtiene los datos de la tabla especificada
        query = text(f"SELECT * FROM {table_name}")
        result = db.session.execute(query)

        # Convierte los resultados en una lista de diccionarios
        columns = result.keys()
        rows = [dict(zip(columns, row)) for row in result]

        return jsonify(rows), 200
    except Exception as e:
        return jsonify({"error": f"Error al obtener datos de la tabla {table_name}: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
