from unittest.mock import MagicMock, patch


def test_index(client):
    response = client.get("/")
    assert b"Hello, Mini Url Fans" in response.data


@patch("mini_url.web.retrieve_mini_url_entity")
def test_redirect_to_url_not_existing_entity(mock_retrieve_mini_url_entity, client):
    mock_retrieve_mini_url_entity.return_value = None
    mock_mini_url_id = "fake-id"

    response = client.get(f"/{mock_mini_url_id}")

    assert b"=(, seems that fake-id is not a valid mini url" in response.data


@patch("mini_url.web.retrieve_mini_url_entity")
@patch("mini_url.web.increment_mini_url_stats")
def test_redirect_to_url_success(
    mock_increment_mini_url_stats, mock_retrieve_mini_url_entity, client
):
    mock_retrieve_mini_url_entity.return_value = MagicMock(
        long_url="http://www.example.com"
    )
    mock_mini_url_id = "fake-id"

    response = client.get(f"/{mock_mini_url_id}")
    assert response.status_code == 302
    mock_increment_mini_url_stats.assert_called()
