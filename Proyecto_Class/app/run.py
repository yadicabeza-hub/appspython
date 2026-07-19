from flask import Flask
from database import db
from flask_migrate import Migrate
import os

def create_app():
    app = Flask(__name__)
    
    # Configuraciones
    # Conexión a MySQL (usando XAMPP por defecto: root sin contraseña)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/sdlc_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-secret-key-sdlc'
    
    db.init_app(app)
    
    # Inicializar Flask-Migrate
    Migrate(app, db)
    
    # Registrar los Blueprints/Rutas desde los controladores
    from controllers.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
