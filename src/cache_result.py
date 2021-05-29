import json
from typing import List, Union
from pathlib import Path

CACHE_PATH='/tmp/ygo-fll.temp'

def cache_result(data: List[dict]) -> None:
    cache = Path(CACHE_PATH)
    cache.write_text(json.dumps(data))

def get_from_cache() -> Union[List[dict], None]:
    cache = Path(CACHE_PATH)

    if not cache.is_file():
        return None

    return json.loads(cache.read_text())

def clear_cache() -> None:
    cache = Path(CACHE_PATH)

    if cache.is_file():
        cache.unlink()
