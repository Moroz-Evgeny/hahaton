import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///User.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.urandom(24)
    
    db.init_app(app)

    # Регистрация Blueprints
    from app.views import main
    from app.register.routes import reg

    app.register_blueprint(reg)
    app.register_blueprint(main)

    return app
