from dataclasses import dataclass
import logging
from scraper import Scraper, ParsedOffer
from typing import Dict, List, Optional
import requests
import json

logging.basicConfig(
    filename="justjoinit.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@dataclass
class LocalizationData:
    """
    Dataclass for storing localization data
    """

    region_id: Optional[int] = None
    city_id: Optional[int] = None
    city_name: Optional[str] = None


class OLXLocalization:
    """
    Fetch localization data from OLX API
    """

    def __init__(self, city_name: str):
        self.city_name = city_name
        self.base_url = (
            f"https://www.olx.pl/api/v1/friendly-links/query-params/{self.city_name}"
        )

    def get_localization_data(self) -> dict | None:
        response = requests.get(self.base_url)
        if response.status_code != 200:
            return None
        return json.loads(response.content)

    def return_localization_data(self) -> LocalizationData | None:
        """
        Returning localization data
        """
        data = self.get_localization_data()
        if data:
            return LocalizationData(
                data["data"]["region_id"],
                data["data"]["city_id"],
                data["metadata"]["names"]["location"]["city"]["name"],
            )
        return None


class OLX(Scraper):
    """
    A scraper for the OLX jobs board.
    """

    def __init__(self, url: str):
        super().__init__(url)

    def fetch_data(self) -> List[Dict[str, str]] | None:
        """
        Fetch data from OLX API.

        Returns:
            A list of dictionaries containing the job offer data, or None if an error occurred.
        """
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            return json.loads(r.content)
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.JSONDecodeError as json_err:
            logging.error(f"JSON decoding error occurred: {json_err}")
        return None

    def parse_offer(self, json_data: List[Dict[str, str]]) -> List[ParsedOffer] | None:
        """
        Parse fetched data and return a list of ParsedOffer objects.

        Args:
            json_data: A list of dictionaries containing the job offer data.

        Returns:
            A list of ParsedOffer objects, or None if an error occurred.
        """

        if not json_data:
            logging.warning("No data received")
            return None

        parsed_data = []
        for data in json_data:
            pass

        return parsed_data


if __name__ == "__main__":
    l = OLXLocalization("Zdunska-wola")
    x = l.return_localization_data()
    print(x)

    # c = JustJoinIT(f"https://www.justjoin.it/api/offers")
    #
    # f = c.fetch_data()
    # parsed_data = c.parse_offer(f)
    # if parsed_data is not None:
    #     logging.info(f"Successfully parsed {len(parsed_data)} job offers")
    #     print(parsed_data)
    # else:
    #     logging.error("Failed to parse job offers")
