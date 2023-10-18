from scrapers import tasks
from typing import List, Optional, Dict, Any


def strategy(country: str) -> List[Optional[Dict[str, Any]]]:
    result = []
    if country == "Poland":
        pracujpl_data = tasks.pracujpl_task()  # TODO add delay
        if pracujpl_data:
            result += pracujpl_data
        olx_data = tasks.olx_task()  # TODO add delay
        if olx_data:
            result += olx_data
    else:
        return []
