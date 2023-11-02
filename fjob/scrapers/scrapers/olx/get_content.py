from ..strategy_abstract.get_content import GetContentStrategy
import logging
import requests
from typing import Optional
import json
from ...models import PageContent

logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class GetOLXContent(GetContentStrategy):
    def __init__(self):
        super().__init__(
            website="OLX",
            base_url="https://www.olx.pl/api/v1/offers?offset=0&limit=40&category_id=4&filter_refiners=spell_checker&sl=18ae25cfa80x3938008f",
        )

    def fetch_content(self) -> None:
        try:
            while self.base_url:
                try:
                    response = requests.get(self.base_url)
                    if response.status_code == 200:
                        json_data = json.loads(response.content)
                        if not json_data:
                            break

                        self.save_to_db_json(json_data)

                        self.base_url = self.get_next_page_url(json_data)
                except Exception as e:
                    logging.error(f"Error occurred: {e}")

        except Exception as e:
            logging.error(f"Error while fetching content from {self.website}")

    @staticmethod
    def get_next_page_url(json_data) -> Optional[str]:
        links = json_data.get("links")
        if links:
            next_page = links.get("next")
            if next_page:
                return next_page.get("href")
        return None
