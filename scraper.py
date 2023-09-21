from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from dataclasses import dataclass


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


class Scraper(ABC):
    def __init__(self, url: str, search: Dict[str, str] = None):
        self.url = url
        self.search = search

    @abstractmethod
    def fetch_data(self, url, search):
        pass

    @abstractmethod
    def parse_data(self, json_data: List[Dict[str, str]]):
        pass

    def save_data(self, data: List[ParsedOffer]):
        pass
        # Implement saving data to database here

