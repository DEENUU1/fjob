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
class ParamsData:
    """
    Dataclass for storing params data
    """

    type: Optional[str] = None
    agreement: Optional[bool] = None
    salary_from: Optional[int] = None
    salary_to: Optional[int] = None
    currency: Optional[str] = None
    experience: Optional[bool] = None
    availability: Optional[str] = None
    workplace: Optional[str] = None


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
        self.params = {
            "offset": "0",
            "sort_by": "created_at:desc",
            "limit": "40",
            "category_id": "4",
        }

    @staticmethod
    def convert_search_query(query: str) -> str:
        return query.replace(" ", "%20")

    def set_param(self, key: str, value: str):
        """
        Set a query parameter for the URL.

        Args:
            key: The parameter key.
            value: The parameter value.
        """
        if key == "query":
            value = self.convert_search_query(value)
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

    def process_description(self, description: str) -> str:
        """
        Delete HTML tags from description
        """
        pass

    def get_params(self, params: List[Dict[str, str]]) -> List[ParamsData]:
        """
        Extract params data from json file
        """
        pass

    def fetch_data(self) -> List[Dict[str, str]] | None:
        """
        Fetch data from OLX API.

        Returns:
            A list of dictionaries containing the job offer data, or None if an error occurred.
        """
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
            parsed_data.append(
                ParsedOffer(
                    title=data["title"],
                    id=data["id"],
                    url=data["url"],
                    description=data["description"],
                )
            )

        return parsed_data


if __name__ == "__main__":
    l = OLXLocalization("Zdunska-wola")
    x = l.return_localization_data()
    print(x)

    olx_scraper = OLX("https://www.olx.pl/api/v1/offers/")
    olx_scraper.set_param("query", "python junior")
    # olx_scraper.set_param("city_id", str(x.city_id))
    # olx_scraper.set_param("region_id", str(x.region_id))
    data = olx_scraper.fetch_data()
    print(olx_scraper.parse_offer(data))

    # c = JustJoinIT(f"https://www.justjoin.it/api/offers")
    #
    # f = c.fetch_data()
    # parsed_data = c.parse_offer(f)
    # if parsed_data is not None:
    #     logging.info(f"Successfully parsed {len(parsed_data)} job offers")
    #     print(parsed_data)
    # else:
    #     logging.error("Failed to parse job offers")
