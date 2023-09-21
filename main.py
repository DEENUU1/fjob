from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedOffer:
    title: Optional[str]
    salary: Optional[int]
    currency: Optional[str]
    source: Optional[str]
    url: Optional[str]
    street:  Optional[str]
    additional_data: ...
    description: Optional[str]
    remote: Optional[bool]
    hybrid: Optional[bool]
    country: Optional[str]
    city: Optional[str]
    date_created: ...
    date_finished: ...
    date_downloaded: ...


class JustJoinIT:
    def __init__(self):
        self.url = f"https://justjoin.it/api/offers"

    def fetch_data(self):
        pass

    def parse_data(self, json_data):
        pass

    def save_data(self, data):
        pass
