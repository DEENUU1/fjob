from ..strategy_abstract.get_content import GetContentStrategy
import logging
import httpx


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class GetTheProtocolContent(GetContentStrategy):
    def __init__(self):
        super().__init__(
            website="TheProtocol", base_url="https://theprotocol.it/?pageNumber="
        )
        self.max_page_num = 55
        self.current_page = 1

    def fetch_content(self) -> None:
        for _ in range(self.current_page, self.max_page_num):
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
