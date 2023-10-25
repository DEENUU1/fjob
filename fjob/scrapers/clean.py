from .scraper import (
    ParsedOffer,
    ParsedWebsite,
    ParsedSalary,
    ParsedLocalization,
    ParsedExperienceLevel,
)
from typing import List, Optional, Dict, Any


class Clean:
    def __init__(self, data: List[Optional[ParsedOffer]]):
        self.data = data
        self.clean_data: List[Optional[ParsedOffer]] = []

    def normalize_experience_name(
        self, data: List[Dict[str, Any]]
    ) -> List[Optional[ParsedExperienceLevel]]:
        pass

    def normalize_salary(
        self, data: List[Dict[str, Any]]
    ) -> List[Optional[ParsedSalary]]:
        pass

    def normalize_localization(
        self, data: List[Dict[str, Any]]
    ) -> List[Optional[ParsedLocalization]]:
        pass

    def get_cleaned_data(self):
        return self.clean_data
