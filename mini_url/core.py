import random
import string
from datetime import datetime

from mini_url import db
from mini_url.dtos import MiniUrlDTO, StatsDTO

MINI_URL_LENGTH = 7


def create_mini_url(url: str) -> MiniUrlDTO:
    """Create a MiniUrlDTO entity from the url specified.

    This method will create an entry in the storage that will be accessed by a
    mini_url_id which is also the key to be used in the main app to get
    redirected to the proper url.
    """
    id = _generate_mini_url_id()
    mini_url_entity = MiniUrlDTO(id, url, datetime.now())
    db.save_mini_url_entity(mini_url_entity)

    return mini_url_entity


def increment_mini_url_stats(mini_url_entity: MiniUrlDTO) -> MiniUrlDTO:
    """Update stats related to the mini url entity after a user used it."""
    if not mini_url_entity.stats:
        mini_url_entity.stats = _generate_first_stats()
    else:
        mini_url_entity.stats.last_time_used = datetime.now()
        mini_url_entity.stats.total_usage += 1

    db.update_mini_url_entity(mini_url_entity)

    return mini_url_entity


def _generate_first_stats() -> StatsDTO:
    return StatsDTO(datetime.now(), 1)


def _generate_mini_url_id():
    return "".join(
        random.choices(string.ascii_letters + string.digits, k=MINI_URL_LENGTH)
    )
