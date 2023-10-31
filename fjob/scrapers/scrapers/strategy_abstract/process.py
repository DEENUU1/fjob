from abc import abstractmethod, ABC
from typing import List, Optional, Dict, Any
from ...scraper import ParsedOffer


class Process(ABC):
    def __init__(self):
        self.processed_data: List[ParsedOffer] = []

    @abstractmethod
    def parse_html(self, html: List[Optional[str]] | Optional[str]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def clean_data(self) -> None:
        pass

    @abstractmethod
    def normalize(self) -> None:
        pass

    def save_to_db(self) -> bool:
        pass
