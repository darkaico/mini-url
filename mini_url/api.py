import http

from flask import Blueprint, Response, json, request

from mini_url.core import create_mini_url, get_url_from_id
from mini_url.dtos import build_json_from_entity

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/mini-url", methods=["POST"])
def mini_url_create_handler():
    data = json.loads(request.data)
    url = data.get("url")

    if not url:
        return Response("Missing url attribute", status=400)

    mini_url_entity = create_mini_url(url)

    return build_json_from_entity(mini_url_entity), http.HTTPStatus.CREATED


@bp.route("/mini-url/<mini_url_id>", methods=["GET"])
def mini_url_retrieve_handler(mini_url_id):
    mini_url_entity = get_url_from_id(mini_url_id)

    if not mini_url_entity:
        return Response("Not Found", status=404)

    return build_json_from_entity(mini_url_entity), http.HTTPStatus.OK
