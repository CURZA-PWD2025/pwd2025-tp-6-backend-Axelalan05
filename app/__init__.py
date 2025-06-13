from flask import Flask
import os
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'a_very_secret_key')

    from .marcas._routes import marcas_bp
    from .categorias._routes import categorias_bp
    from .proveedores._routes import proveedores_bp
    from .articulos._routes import articulos_bp

    app.register_blueprint(marcas_bp, url_prefix='/api/marcas')
    app.register_blueprint(categorias_bp, url_prefix='/api/categorias')
    app.register_blueprint(proveedores_bp, url_prefix='/api/proveedores')
    app.register_blueprint(articulos_bp, url_prefix='/api/articulos')

    return app