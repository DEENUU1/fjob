from bs4 import BeautifulSoup
import httpx
from typing import List, Dict, Any, Optional
from ..scraper import Scraper, ParsedOffer

BASE_URL = f"https://www.praca.pl/oferty-pracy_"
extract_data_list = []


def get_max_page() -> int:
    response = httpx.get(f"{BASE_URL}1")
    soup = BeautifulSoup(response.text, "html.parser")
    pagination = soup.find("a", class_="pagination__item--last")
    if pagination:
        return int(pagination.text)
    else:
        return 1


class PracaPL(Scraper):
    def __init__(self, url: str, max_page: int = 2):
        super().__init__(url)
        self.max_page = max_page

    def fetch_data(self) -> str:
        response = httpx.get(f"{BASE_URL}{self.max_page}")
        return response.text

    @staticmethod
    def extract_data(data: str) -> None:
        if not data:
            return

        soup = BeautifulSoup(data, "html.parser")
        offers = soup.find_all("li", class_="listing__item")

        for offer in offers:
            offer_data = {}

            title_element = offer.find("a", class_="listing__title")
            work_mode_element = offer.find("span", class_="listing__work-model")
            localization_element = offer.find("span", class_="listing__location-name")
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

            extract_data_list.append(offer_data)

    def pipeline(self) -> None:
        # for i in range(1, max_page + 1):
        for i in range(1, self.max_page):
            fetched_data = self.fetch_data()
            self.extract_data(fetched_data)
