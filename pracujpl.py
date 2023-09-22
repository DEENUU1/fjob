from dataclasses import dataclass
import logging
from scraper import Scraper, ParsedOffer
from typing import Dict, List, Optional, Any
import requests
import json

logging.basicConfig(
    filename="justjoinit.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class PracujPL(Scraper):
    """
    A scraper for the Pracuj.pl jobs board.
    """

    def __init__(self, url: str):
        super().__init__(url)
        self.params = {}

    @staticmethod
    def convert_search_query(query: str) -> str:
        return query.replace(" ", "+")

    @staticmethod
    def get_region_id(region: str) -> int:
        pass

    @staticmethod
    def convert_city_name(city: str) -> str:
        return city.replace(" ", "+")

    def set_param(self, key: str, value: str):
        """
        Set a query parameter for the URL.

        Args:
            key: The parameter key.
            value: The parameter value.
        """
        if key == "query":
            value = self.convert_search_query(value)
        elif key == "r":  # Region
            value = ...
        elif key == "wp":  # City
            value = ...
        self.params[key] = value

    def build_url(self) -> str:
        """
        Build the URL to be used for scraping.

        Returns:
            The URL to be used for scraping.
        """
        url = self.url
        if self.params:
            param_string = "&".join(
                [f"{key}={value}" for key, value in self.params.items()]
            )
            url += f"?{param_string}"
        return url

    def fetch_data(self) -> List[Dict[str, str]] | None:
        try:
            r = requests.get(self.build_url())
            r.raise_for_status()
            return json.loads(r.content)
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.JSONDecodeError as json_err:
            logging.error(f"JSON decoding error occurred: {json_err}")
        return None

    def parse_offer(self, json_data: Dict[str, List]) -> List[ParsedOffer] | None:
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
        for data in json_data["data"]:
            pass

        return parsed_data


if __name__ == "__main__":
    scraper = PracujPL("https://massachusetts.pracuj.pl/jobOffers/listing/")
    # # olx_scraper.set_param("query", "python junior")
    # scraper.set_param("city_id", str(x.city_id))
    # scraper.set_param("region_id", str(x.region_id))
    # data = scraper.fetch_data()
    # result = scraper.parse_offer(data)
    #
    # if result is not None:
    #     logging.info(f"Successfully parsed {len(result)} job offers")
    #     print(result)
    # else:
    #     logging.error("Failed to parse job offers")
