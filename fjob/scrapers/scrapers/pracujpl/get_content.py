from ..strategy_abstract.get_content import GetContentStrategy
import logging
import httpx
from bs4 import BeautifulSoup


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_max_page_number() -> int:
    try:
        response = httpx.get(f"https://it.pracuj.pl/praca")
        soup = BeautifulSoup(response.text, "html.parser")
        max_page_element = soup.find(
            "span", {"data-test": "top-pagination-max-page-number"}
        )
        if max_page_element:
            return int(max_page_element.text)
    except Exception as e:
        logging.error(f"Error while fetching max page number for PracujPL - {e}")

    return 1


class GetPracujPLContent(GetContentStrategy):
    def __init__(self, max_page):
        super().__init__(website="PracujPL", base_url="https://it.pracuj.pl/praca")
        self.max_page = max_page
        self.current_page = 1

    def fetch_content(self) -> None:
        for _ in range(self.current_page, self.max_page):
            try:
                response = httpx.get(f"{self.base_url}{self.current_page}")
                self.data.append(response.text)
                self.current_page += 1
                logging.info(
                    f"Fetched content from {self.website} - page: {self.current_page}"
                )
            except Exception as e:
                logging.error(
                    f"Error while fetching content from {self.website} - page: {self.current_page} - {e}"
                )
