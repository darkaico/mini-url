from datetime import datetime
from unittest.mock import patch

import pytest

from mini_url.core import (
    _generate_first_stats,
    _generate_mini_url_id,
    increment_mini_url_stats,
)
from mini_url.dtos import MiniUrlDTO


@pytest.fixture
def mini_url():
    return MiniUrlDTO("id", "https://www.marvel.com", datetime.now())


def test_generate_mini_url_id_are_different():
    id_one = _generate_mini_url_id()
    id_two = _generate_mini_url_id()

    assert id_one != id_two


def test_generate_mini_url_id_size():
    random_id = _generate_mini_url_id()

    # This test here is checking the number directly and not the constant in order
    # to confirm by updating the tests that the size of the id was updated with confidence
    assert len(random_id) == 7


def test_generate_first_stats():
    stats = _generate_first_stats()

    assert stats.total_usage == 1
    assert isinstance(stats.last_time_used, datetime)


@patch("mini_url.core.db.update_mini_url_entity")
def test_increment_mini_url_stats_first_time(mock_update_mini_url_entity, mini_url):
    mini_url_updated = increment_mini_url_stats(mini_url)

    assert mini_url_updated.stats.total_usage == 1

    mock_update_mini_url_entity.assert_called()