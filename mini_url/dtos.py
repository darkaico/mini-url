import datetime
import json
from dataclasses import asdict, dataclass, is_dataclass


@dataclass
class StatsDTO:
    last_time_used: datetime
    total_usage: int


@dataclass
class MiniUrlDTO:
    id: str
    long_url: str
    created: datetime.datetime
    stats: StatsDTO = None


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        elif isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()

        return super().default(obj)


def build_json_from_entity(dto_entity: dataclass) -> dict:

    json_str = json.dumps(dto_entity, cls=EnhancedJSONEncoder)

    return json.loads(json_str)
