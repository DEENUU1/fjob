import httpx
from bs4 import BeautifulSoup
from ..scraper import Scraper, ParsedOffer
from typing import List, Dict, Any, Optional
import logging


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


BASE_URL = "https://theprotocol.it/?pageNumber="
MAX_PAGE_NUM = 58


class TheProtocol(Scraper):
    def __init__(self):
        super().__init__(url=BASE_URL)
        self.page_num = 1
        self.data = []

    def fetch_data(self) -> Optional[str]:
        try:
            response = httpx.get(f"{BASE_URL}{self.page_num}")
            return response.text
        except Exception as e:
            logging.error(f"Error occurred during fetching data: {e}")
            return None

    def parse_data(self, response: str) -> None:
        try:
            soup = BeautifulSoup(response, "html.parser")
            job_cards = soup.find_all("a", class_="anchorClass_a6of9et")
        except Exception as e:
            logging.error(f"Error occurred during extracting data: {e}")
            return None

        try:
            for card in job_cards:
                offer_data = {}

                title = card.find("h2", class_="titleText_t1280ha4")
                url = card.get("href")
                company_logo = card.find("img")
                details = card.find_all("div", class_="rootClass_rpqnjlt")
                skill_divs = card.find_all(
                    "div", {"data-test": "chip-expectedTechnology"}
                )
                skills = []
                if skill_divs:
                    for div in skill_divs:
                        spans = div.find_all("span", class_="Label_l1fs6hs4")
                        for span in spans:
                            skills.append(span.text)
                localization = card.find("div", {"data-test": "text-workplaces"})
                d = {}
                for idx, detail in enumerate(details):
                    if idx == 0:
                        d["company_name"] = detail

                    if idx == 1:
                        d["work_mode"] = detail
                if title:
                    offer_data["title"] = title.text
                if company_logo:
                    offer_data["company_logo"] = company_logo["src"]
                if d.get("company_name", None):
                    offer_data["company_name"] = d["company_name"].text
                if d.get("work_mode", None):
                    offer_data["work_mode"] = d["work_mode"].text
                if skills:
                    offer_data["skills"] = skills
                if localization:
                    offer_data["localization"] = localization.text
                if url:
                    offer_data["url"] = url
                self.data.append(offer_data)
        except Exception as e:
            logging.error(f"Error occurred during parsing data: {e}")
            return None

    def parse_offer(self, data: List[Dict[str, Any]]) -> List[Optional[ParsedOffer]]:
        parsed_offers = []
        try:
            for offer in data:
                parsed_offers.append(
                    ParsedOffer(
                        title=offer.get("title", None),
                        company_name=offer.get("company_name", None),
                        company_logo=offer.get("company_logo", None),
                        skills=offer.get("skills", None),
                        city=offer.get("localization", None),
                        url=f"{'https://theprotocol.it/'}{offer.get('url', None)}",
                    )
                )
        except Exception as e:
            logging.error(f"Error occurred during parsing offer: {e}")
            return []

        return parsed_offers

    def pipeline(self) -> List[Optional[ParsedOffer]]:
        try:
            for i in range(1, MAX_PAGE_NUM):
                response = self.fetch_data()
                self.parse_data(response)
                self.page_num += 1

            logging.info(f"Parsed {len(self.data)} offers from theprotocol.it")
            return self.parse_offer(self.data)
        except Exception as e:
            logging.error(f"Error occurred during pipeline: {e}")
            return []
