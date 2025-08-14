from flask import Flask
from .admin import admin_bp
from .main import main_bp
from .usuario import usuario_bp

def create_app():

    app = Flask(__name__)

    app.secret_key = "ChaveMaisSeguraDoMundo"

    
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(main_bp)
    app.register_blueprint(usuario_bp, url_prefix="/usuario")

    return app