from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class ParsedOffer:
    title: Optional[str] = None
    salary_from: Optional[int] = None
    salary_to: Optional[int] = None
    currency: Optional[str] = None
    url: Optional[str] = None
    street:  Optional[str] = None
    additional_data: Optional[Dict[str, str]] = None
    description: Optional[str] = None
    remote: Optional[bool] = None
    hybrid: Optional[bool] = None
    country: Optional[str] = None
    city: Optional[str] = None
    date_created: Optional[str] = None
    date_finished: Optional[str] = None
    experience_level: Optional[str] = None
    skills: Optional[List[str]] = None

class Scraper(ABC):
    def __init__(self, url: str, search: Dict[str, str] = None):
        self.url = url
        self.search = search

    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def parse_data(self, json_data: List[Dict[str, str]]):
        pass

    def save_data(self, data: List[ParsedOffer]):
        pass
        # Implement saving data to database here

