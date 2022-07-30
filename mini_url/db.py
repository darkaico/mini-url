from dataclasses import asdict
from flask_pymongo import PyMongo
from flask import current_app, g
from mini_url.dtos import MiniUrlDTO, build_json_from_entity

mongo = None


def get_db_client():
    if "db" not in g:
        g.db = PyMongo(current_app)

    return g.db


def save_mini_url_entity(mini_url_entity: MiniUrlDTO) -> MiniUrlDTO:
    mongo = get_db_client()

    mongo.db.miniUrls.insert_one(
        {
            "_id": mini_url_entity.id,
            "long_url": mini_url_entity.long_url,
            "created": mini_url_entity.created,
        }
    )

    return mini_url_entity


def retrieve_mini_url_entity(mini_url_id: str) -> MiniUrlDTO:
    mongo = get_db_client()

    db_row = mongo.db.miniUrls.find_one({"_id": mini_url_id})
    if db_row:
        return MiniUrlDTO(
            db_row["_id"], db_row["long_url"], db_row["created"], db_row.get("stats")
        )

    return None


def update_mini_url_entity(mini_url_entity: MiniUrlDTO):
    mongo = get_db_client()

    mini_url_dict = asdict(mini_url_entity)
    mini_url_dict.pop("id", None)

    mongo.db.miniUrls.update_one({"_id": mini_url_entity.id}, {"$set": mini_url_dict})
