import os

from flask import Flask, redirect
from mini_url.api import bp as api_bp
from mini_url.core import increment_mini_url_stats
from mini_url.db import retrieve_mini_url_entity

from .settings import config


def create_app(config_name=None) -> Flask:
    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "development")

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    @app.route("/")
    def index():
        return "Hello, Mini Url Fans!"

    @app.route("/<mini_url_id>")
    def redirect_to_url(mini_url_id):
        mini_url_entity = retrieve_mini_url_entity(mini_url_id)
        if not mini_url_entity:
            return f"=(, seems that {mini_url_id} is not a valid mini url"

        increment_mini_url_stats(mini_url_entity)

        return redirect(mini_url_entity.long_url)

    app.register_blueprint(api_bp)

    return app
