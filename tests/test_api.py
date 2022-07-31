from datetime import datetime
from unittest.mock import patch

import pytest

from mini_url.dtos import MiniUrlDTO


@pytest.fixture
def mini_url():
    return MiniUrlDTO("id", "https://www.marvel.com", datetime.now())


@patch("mini_url.api.retrieve_mini_url_entity")
def test_retrieve_mini_url_found(mock_retrieve_mini_url_entity, client, mini_url):
    mock_retrieve_mini_url_entity.return_value = mini_url
    mock_mini_url_id = "fake-id"

    response = client.get(f"/api/mini-url/{mock_mini_url_id}")

    assert response.status_code == 200
    assert response.json["id"] == mini_url.id
    assert response.json["long_url"] == mini_url.long_url


@patch("mini_url.api.retrieve_mini_url_entity")
def test_retrieve_mini_url_not_found(mock_retrieve_mini_url_entity, client, mini_url):
    mock_retrieve_mini_url_entity.return_value = None
    mock_mini_url_id = "fake-id"

    response = client.get(f"/api/mini-url/{mock_mini_url_id}")

    assert response.status_code == 404


def test_create_mini_url_invalid(client):

    response = client.post("/api/mini-url", json={})

    assert response.status_code == 400
    assert response.json["url"] == "this attribute is required"


@patch("mini_url.api.create_mini_url")
def test_create_mini_url_valid(mock_create_mini_url, client, mini_url):
    mock_create_mini_url.return_value = mini_url
    response = client.post("/api/mini-url", json={"url": "https://www.marvel.com"})

    assert response.status_code == 201
    assert response.json["id"] is not None
    assert response.json["long_url"] == "https://www.marvel.com"
