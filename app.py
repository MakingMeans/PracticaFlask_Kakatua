# app.py
from flask import Flask
from models import db  # Importa la instancia de db desde models


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mainuser:1234@192.168.1.80:5432/nominadb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar SQLAlchemy con la app
    db.init_app(app)

    with app.app_context():
        # Crear tablas si no existen
        db.create_all()

    # Importar y registrar las rutas
    from routes import register_routes
    register_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
