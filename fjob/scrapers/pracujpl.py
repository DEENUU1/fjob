import logging
from .scraper import Scraper, ParsedOffer, Salary
from typing import Dict, List, Optional
import requests
import json

logging.basicConfig(
    filename="../logs.log",
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
        """Replace spaces with '+' in search query.

        Args:
            query: The search query.

        Returns:
            The search query with spaces replaced with '+'.
        """
        return query.replace(" ", "+")

    @staticmethod
    def convert_city_name(city: str) -> str:
        """Replace spaces with '+' in city name.

        Args:
            city: The city name.

        Returns:
            The city name with spaces replaced with '+'.
        """
        return city.replace(" ", "+")

    @staticmethod
    def convert_region_name(region: str) -> str:
        """Replace spaces with '-' in region name.

        Args:
            region: The region name.

        Returns:
            The region name with spaces replaced with '-'.
        """
        return region.replace(" ", "-")

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

    def fetch_data(self) -> Optional[Dict[str, List[Dict[str, str]]]]:
        try:
            r = requests.get(self.build_url())
            r.raise_for_status()
            return json.loads(r.content)
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.JSONDecodeError as json_err:
            logging.error(f"JSON decoding error occurred: {json_err}")
        return None

    @staticmethod
    def check_work_mode(datas: List[str]):
        """Check if hybrid or remote work mode are available."""
        is_hybrid = False
        is_remote = False

        for data in datas:
            if "zdalna" in data:
                is_remote = True
            elif "hybrydowa" in data:
                is_hybrid = True

        return is_hybrid, is_remote

    def parse_offer(
        self, json_data: Optional[Dict[str, List[Dict[str, str]]]]
    ) -> List[ParsedOffer] | None:
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
        for data in json_data["groupedOffers"]:
            is_hybrid, is_remote = self.check_work_mode(data["workModes"])

            salary = Salary(
                contract_type=data["typesOfContract"][0],
                work_schedule=data["workSchedules"][0],
            )

            parsed_data.append(
                ParsedOffer(
                    title=data["jobTitle"],
                    salary=[salary],
                    url=data["offers"][0]["offerAbsoluteUri"],
                    remote=is_remote,
                    hybrid=is_hybrid,
                    country="PL",
                    city=data["offers"][0]["displayWorkplace"],
                    date_created=data["lastPublicated"],
                    date_finished=data["expirationDate"],
                    description=data["jobDescription"],
                    company_name=data["companyName"],
                    company_logo=data["companyLogoUri"],
                    experience_level=data["positionLevels"][0],
                )
            )

        return parsed_data


def run(sfd: bool, spd: bool, city: str, query: str = None, region: str = None) -> None:
    scraper = PracujPL("https://massachusetts.pracuj.pl/jobOffers/listing/multiregion")

    if query:
        scraper.set_param("query", query)
    elif region and city:
        scraper.set_param("wp", region)
    elif region:
        scraper.set_param("wp", region)
    elif city:
        scraper.set_param("wp", city)

    logging.info(f"Start fetching data for {scraper.url}")
    data = scraper.fetch_data()

    if data is None:
        logging.error("Failed to fetch data")
    else:
        logging.info(f"Scraped {len(data)} job offers")

        if sfd:
            logging.info(f"Saving fetch data to json")
            scraper.save_fetch_data_to_json(data)
            logging.info(f"Fetch data saved to json")

        logging.info("Start parsing data")
        result = scraper.parse_offer(data)

        if result is None:
            logging.error("Failed to parse job offers")
        else:
            logging.info(f"Successfully parsed {len(result)} job offers")

            if spd:
                logging.info(f"Saving parsed data to json")
                scraper.save_parsed_data_to_json(result)
                logging.info("Parsed data saved to json")
