from ..strategy_abstract.get_content import GetContentStrategy
import logging
import httpx
from bs4 import BeautifulSoup


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_max_page() -> int:
    try:
        response = httpx.get(f"https://www.praca.pl/oferty-pracy_1")
        soup = BeautifulSoup(response.text, "html.parser")
        pagination = soup.find("a", class_="pagination__item--last")
        if pagination:
            logging.info(f"Get max page for PracaPL: {int(pagination.text)}")
            return int(pagination.text)
        else:
            return 1
    except Exception as e:
        logging.error(f"Error occurred during getting max page for PracaPL: {e}")

    return 1


class GetPracaPLContent(GetContentStrategy):
    def __init__(self, max_page: int):
        super().__init__(
            website="PracaPL", base_url="https://www.praca.pl/oferty-pracy_"
        )
        self.max_page = max_page
        self.current_page = 1

    def fetch_content(self) -> None:
        for _ in range(self.current_page, self.max_page + 1):
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
