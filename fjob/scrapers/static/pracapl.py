from bs4 import BeautifulSoup
import httpx
from typing import List, Dict, Any, Optional, Tuple
from ..scraper import Scraper, ParsedOffer
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
    def __init__(self, url: str = BASE_URL, max_page: int = 2):
        super().__init__(url)
        self.max_page = max_page
        self.extract_data_list = []

    def fetch_data(self) -> Optional[str]:
        try:
            response = httpx.get(f"{BASE_URL}{self.max_page}")
            return response.text
        except Exception as e:
            logging.error(f"Error occurred during fetching data: {e}")
            return None

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
        try:
            for data in data_list:
                hybrid, remote = self.is_remote_hybrid(data.get("localization", ""))
                localization = self.parse_localization(data.get("localization", ""))

                parsed_offers.append(
                    ParsedOffer(
                        title=data.get("title", ""),
                        url=data.get("url", ""),
                        city=localization if localization else None,
                        company_name=data.get("employer_name", ""),
                        company_logo=data.get("employer_img", ""),
                        remote=remote,
                        hybrid=hybrid,
                    )
                )
        except Exception as e:
            logging.error(f"Error occurred during parsing data: {e}")
            return []
        return parsed_offers

    def pipeline(self) -> None:
        try:
            for i in range(1, self.max_page + 1):
                fetched_data = self.fetch_data()
                self.extract_data(fetched_data)

            parsed_data = self.parse_offer(self.extract_data_list)
            self.save_data(parsed_data)
        except Exception as e:
            logging.error(f"An error occurred while scraping data from pracapl {e}")
