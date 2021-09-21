from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .auth.v1 import version1
from config import config_options

db=SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.register_blueprint(version1)

    app.config.from_object(config_options[config_name])
    db.init_app(app)

    return app