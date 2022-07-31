from flask import Blueprint, redirect

from mini_url.core import increment_mini_url_stats
from mini_url.db import retrieve_mini_url_entity

bp = Blueprint("web", __name__, url_prefix="/")


@bp.route("/")
def index():
    return "Hello, Mini Url Fans!"


@bp.route("/<mini_url_id>")
def redirect_to_url(mini_url_id):
    mini_url_entity = retrieve_mini_url_entity(mini_url_id)
    if not mini_url_entity:
        return f"=(, seems that {mini_url_id} is not a valid mini url"

    increment_mini_url_stats(mini_url_entity)

    return redirect(mini_url_entity.long_url)
