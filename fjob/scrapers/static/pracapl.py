from bs4 import BeautifulSoup
import httpx
from typing import List, Dict, Any, Optional, Tuple
from ..scraper import (
    Scraper,
    ParsedOffer,
    ParsedLocalization,
    ParsedSalary,
    ParsedWebsite,
    ParsedExperienceLevel,
)
import logging


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


BASE_URL = f"https://www.praca.pl/oferty-pracy_"


def get_max_page() -> int:
    try:
        response = httpx.get(f"{BASE_URL}1")
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.find("a", class_="pagination__item--last")
        if pagination:
            return int(pagination.text)
        else:
            return 1
    except Exception as e:
        logging.error(f"Error occurred during getting max page: {e}")

    return 1


class PracaPL(Scraper):
    def __init__(self, max_page: int, url: str = BASE_URL):
        super().__init__(url)
        self.max_page = max_page
        self.page = 1
        self.extract_data_list = []

    def fetch_data(self) -> Optional[str]:
        try:
            response = httpx.get(f"{BASE_URL}{self.page}")
            return response.text
        except Exception as e:
            logging.error(f"Error occurred during fetching data: {e}")
            return None

    @staticmethod
    def get_experience_levels(data: str) -> Optional[str]:
        result = None

        if not data:
            return result

        if "mid" in data:
            result = "Mid"
        if "senior" in data:
            result = "Senior"
        if "asystent" in data:
            result = "Asystent"
        if "pracownik fizyczny" in data:
            result = "Pracownik fizyczny"
        if "praktykant/stażysta" in data:
            result = "Praktykant/stażysta"
        if "asystent" in data:
            result = "Asystent"
        if "junuior" in data:
            result = "Junior"
        if "ekspert" in data:
            result = "Ekspert"
        if "kierownik/koordynator" in data:
            result = "Kierownik/koordynator"
        if "menedżer" in data:
            result = "Menedżer"
        if "dyrektor" in data:
            result = "Dyrektor"
        if "prezes" in data:
            result = "Prezes"

        return result

    @staticmethod
    def get_contract_type(data: str) -> Optional[str]:
        result = None
        if not data:
            return result

        if "umowa o prace" in data:
            result = "Umowa o prace"
        if "umowa o dzieło" in data:
            result = "Umowa o dzieło"
        if "umowa zlecenie" in data:
            result = "Umowa zlecenie"
        if "kontrakt B2B" in data:
            result = "Kontrakt B2B"
        if "umowa o pracę tymczasową" in data:
            result = "Umowa o pracę tymczasową"
        if "umowa agencyjna" in data:
            result = "Umowa agencyjna"
        if "umowa o staż/praktykę" in data:
            result = "Umowa o staż/praktykę"
        if "umowa na zastępstwo" in data:
            result = "Umowa na zastępstwo"

        return result

    @staticmethod
    def get_work_schedule(data: str) -> Optional[str]:
        result = None
        if not data:
            return result

        if "pełny etat" in data:
            result = "Pełny etat"
        if "część etatu" in data:
            result = "Część etatu"
        if "tymczasowa/dodatkowa" in data:
            result = "Tymczasowa/dodatkowa"

        return result

    def extract_data(self, data: str) -> None:
        if not data:
            return

        try:
            soup = BeautifulSoup(data, "html.parser")
            offers = soup.find_all("li", class_="listing__item")
        except Exception as e:
            logging.error(f"Error occurred during extracting data: {e}")
            return None

        try:
            for offer in offers:
                offer_data = {}

                title_element = offer.find("a", class_="listing__title")
                work_mode_element = offer.find("span", class_="listing__work-model")
                localization_element = offer.find(
                    "span", class_="listing__location-name"
                )
                employer_name_element = offer.find("a", class_="listing__employer-name")
                employer_img_element = offer.find("img", class_="listing__logo")
                details_element = offer.find("div", class_="listing__main-details")

                if details_element:
                    offer_data["details"] = details_element.text
                if title_element:
                    offer_data["title"] = title_element.text
                    offer_data["url"] = title_element.get("href")
                if work_mode_element:
                    offer_data["work_mode"] = work_mode_element.text
                if localization_element:
                    offer_data["localization"] = localization_element.text
                if employer_img_element:
                    offer_data["employer_img"] = employer_img_element.get("src")
                if employer_name_element:
                    offer_data["employer_name"] = employer_name_element.text

                self.extract_data_list.append(offer_data)
        except Exception as e:
            logging.error(f"Error occurred during extracting data: {e}")
            return None

    @staticmethod
    def is_remote_hybrid(data: str) -> Tuple[bool, bool]:
        if not data:
            return False, False

        hybrid = False
        remote = False
        if "hybrydowa" in data:
            hybrid = True

        if "zdalna" in data:
            remote = True

        return hybrid, remote

    @staticmethod
    def parse_localization(data: str) -> Optional[str]:
        if not data:
            return None

        city = data.split()[0]
        return city

    def parse_offer(
        self, data_list: List[Dict[str, Any]]
    ) -> List[Optional[ParsedOffer]]:
        parsed_offers = []
        if not data_list:
            return []

        website = ParsedWebsite(name="Praca.pl", url="https://www.praca.pl")
        try:
            for data in data_list:
                hybrid, remote = self.is_remote_hybrid(data.get("localization", ""))
                localization = self.parse_localization(data.get("localization", ""))
                experience_data = self.get_experience_levels(data.get("details", ""))
                contract_type = self.get_contract_type(data.get("details", ""))
                work_schedule = self.get_work_schedule(data.get("details", ""))

                experience = ParsedExperienceLevel(name=experience_data)
                salary = ParsedSalary(
                    contract_type=contract_type, work_schedule=work_schedule
                )
                localization = ParsedLocalization(city=localization, country="Poland")

                parsed_offers.append(
                    ParsedOffer(
                        title=data.get("title", ""),
                        url=data.get("url", ""),
                        company_name=data.get("employer_name", ""),
                        company_logo=data.get("employer_img", ""),
                        is_remote=remote,
                        is_hybrid=hybrid,
                        salary=[salary],
                        website=website.url,
                        localizations=[localization],
                        experience_level=[experience],
                    )
                )
        except Exception as e:
            logging.error(f"Error occurred during parsing data: {e}")
            return []
        return parsed_offers

    def pipeline(self) -> List[Optional[ParsedOffer]]:
        try:
            for i in range(1, self.max_page + 1):
                fetched_data = self.fetch_data()
                self.extract_data(fetched_data)
                self.page += 1
            logging.info(f"Parsed {len(self.extract_data_list)} offers from pracapl")
            return self.parse_offer(self.extract_data_list)
        except Exception as e:
            logging.error(f"An error occurred while scraping data from pracapl {e}")
            return []
