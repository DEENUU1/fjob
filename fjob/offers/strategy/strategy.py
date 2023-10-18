from scrapers import tasks
from typing import List, Optional, Dict, Any


def strategy(
    country: str, city: str, user, query: str = None
) -> List[Optional[Dict[str, Any]]]:
    result = []
    if country == "Poland":
        pracujpl_data = tasks.pracujpl_task(
            city=city, query=query, user=user
        )  # TODO add delay
        if pracujpl_data:
            result += pracujpl_data
        olx_data = tasks.olx_task(city=city, query=query, user=user)  # TODO add delay
        if olx_data:
            result += olx_data
    else:
        return []

    return result
