from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.Config')
    mongo = PyMongo(app)

    with app.app_context():
        from .routes.api import api_bp
        app.register_blueprint(api_bp, url_prefix='/api')

    return app
