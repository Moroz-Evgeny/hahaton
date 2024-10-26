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
    from app.index.routes import ind
    from app.transaction.routes import trans
    from app.api import api
    from app.profile.routes import prof

    app.register_blueprint(prof)
    app.register_blueprint(api)
    app.register_blueprint(trans)
    app.register_blueprint(ind)
    app.register_blueprint(main)

    return app
