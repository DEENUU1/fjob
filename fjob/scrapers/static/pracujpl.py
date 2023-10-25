import logging
from typing import Dict, Optional, Tuple, List
from bs4 import BeautifulSoup

import requests
import re

from ..scraper import (
    Scraper,
    ParsedOffer,
    ParsedWebsite,
    ParsedSalary,
    ParsedLocalization,
    ParsedExperienceLevel,
)

logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class PracujPLIT(Scraper):
    """
    A scraper for the Pracuj.pl jobs board.
    """

    def __init__(self, url: str = "https://it.pracuj.pl/praca") -> None:
        super().__init__(url)
        self.max_page_number = None

    def fetch_data(self) -> Optional[str]:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logging.error(f"Error occurred: {e}")
        return None

    @staticmethod
    def get_max_page_number(data: str) -> Optional[int]:
        if not data:
            return None

        soup = BeautifulSoup(data, "html.parser")
        max_page_element = soup.find(
            "span", {"data-test": "top-pagination-max-page-number"}
        )
        if max_page_element:
            return int(max_page_element.text)
        return None

    def run(self) -> None:
        data = self.fetch_data()
        if data:
            self.max_page_number = self.get_max_page_number(data)

        if self.max_page_number:
            for page in range(1, self.max_page_number + 1):
                self.url = f"https://it.pracuj.pl/praca?pn={page}"
                data = self.fetch_data()
                if data:
                    parsed_data = self.parse_offer(data)
                    print(parsed_data)
                    # self.save_data(parsed_data)
                else:
                    logging.info("No data received")

    @staticmethod
    def get_experience_level(data: List[str]) -> Optional[str]:
        if not data:
            return None

        if "Mid" in data:
            return "Mid"
        if "Senior" in data:
            return "Senior"
        if "Junior" in data:
            return "Junior"
        if "Praktykant" in data:
            return "Praktykant"
        if "Stażysta" in data:
            return "Stażysta"

    @staticmethod
    def is_remote(data: List[str]) -> bool:
        if "Praca zdalna" in data:
            return True
        return False

    @staticmethod
    def is_hybrid(data: List[str]) -> bool:
        if "Praca hybrydowa" in data:
            return True
        return False

    @staticmethod
    def get_contract_type(data: List[str]) -> List[Optional[str]]:
        result = []
        if not data:
            return []

        if "Umowa o pracę" in data:
            result.append("Umowa o pracę")
        elif "Umowa zlecenie" in data:
            result.append("Umowa zlecenie")
        elif "Umowa o dzieło" in data:
            result.append("Umowa o dzieło")
        elif "Kontrakt B2B" in data:
            result.append("Kontrakt B2B")
        elif "Umowa o zastępstwo" in data:
            result.append("Umowa o zastępstwo")
        elif "Umowa agencyjna" in data:
            result.append("Umowa agencyjna")
        elif "Umowa o pracę tymczasową" in data:
            result.append("Umowa o pracę tymczasową")
        elif "Umowa o staż / praktyki" in data:
            result.append("Umowa o staż / praktyki")

        return result

    @staticmethod
    def parse_localization(text: str) -> Optional[str]:
        result = None
        if not text:
            return None

        if "localizacji":
            result = None

        split_data = text.split()
        if len(split_data) == 1:
            result = text
        else:
            result = split_data[0]

        return result

    def parse_offer(self, data: str) -> List[ParsedOffer]:
        parsed_data = []

        soup = BeautifulSoup(data, "html.parser")
        offers_section = soup.find("div", {"data-test": "section-offers"})
        if offers_section:
            offers = offers_section.find_all(
                "div", class_="listing-it_bp811tr listing-it_po9665q"
            )

            if offers:
                for offer in offers:
                    title = None
                    additional_data = None
                    url = None
                    parsed_localization = None
                    skills_list = None
                    company_logo = None
                    company_name = None

                    title_element = offer.find(
                        "a", class_="listing-it_o1bdr2ew listing-it_n194fgoq"
                    )
                    company_element = offer.find("img", class_="listing-it_ia9ocxs")
                    skills_container = offer.find(
                        "div", {"data-test": "technologies-list"}
                    )
                    additional_data_container = offer.find(
                        "ul", class_="listing-it_b1ef77ng"
                    )
                    localization_element = offer.find(
                        "h5", {"date-test": "text-region"}
                    )

                    if localization_element:
                        localization_text = localization_element.text
                        parsed_localization = self.parse_localization(localization_text)

                    if additional_data_container:
                        additional_data_list = additional_data_container.find_all("li")
                        if additional_data_list:
                            additional_data = [
                                data.text for data in additional_data_list
                            ]

                    if skills_container:
                        skills = skills_container.find_all(
                            "span", {"data-test": "technologies-item"}
                        )
                        if skills:
                            skills_list = [skill.text for skill in skills]

                    if company_element:
                        company_logo = company_element.get("src")
                        company_name = company_element.get("alt")
                    if title_element:
                        url = title_element.get("href")
                        title = title_element.text

                    salaries = []
                    if additional_data:
                        contracts = self.get_contract_type(additional_data)
                        for contract in contracts:
                            salaries.append(Salary(contract_type=contract))

                    parsed_data.append(
                        ParsedOffer(
                            title=title if title else None,
                            url=url if url else None,
                            remote=self.is_remote(additional_data)
                            if additional_data
                            else None,
                            hybrid=self.is_hybrid(additional_data)
                            if additional_data
                            else None,
                            country="PL",
                            additional_data=additional_data
                            if additional_data
                            else None,
                            salary=salaries if salaries else None,
                            city=parsed_localization if parsed_localization else None,
                            skills=skills_list if skills_list else None,
                            company_name=company_name if company_name else None,
                            company_logo=company_logo if company_logo else None,
                            experience_level=self.get_experience_level(additional_data)
                            if additional_data
                            else None,
                        )
                    )

        return parsed_data
