import os

from flask import Flask

from mini_url.api import bp as api_bp
from mini_url.web import bp as web_bp

from .settings import config


def create_app(config_name=None) -> Flask:
    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "development")

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)

    return app
