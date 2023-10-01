import json
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional, Any

import requests

from .scraper import Scraper, ParsedOffer, Salary

logging.basicConfig(
    filename="../logs.log",
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


@dataclass
class Localization:
    """
    Dataclass for storing localization data
    """

    region: Optional[str] = None
    city: Optional[str] = None


class OLXLocalization:
    """
    Fetch localization data from OLX API
    """

    def __init__(self, city_name: str):
        self.city_name = city_name.replace(" ", "-").lower()
        self.base_url = (
            f"https://www.olx.pl/api/v1/friendly-links/query-params/{self.city_name}"
        )

    def get_localization_data(self) -> dict | None:
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return json.loads(response.content)
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error occurred: {e}")
            return None

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

    @staticmethod
    def process_description(description: str) -> str:
        """
        Delete HTML tags from description
        """
        return (
            description.replace("<p>", " ")
            .replace("</p>", " ")
            .replace("<strong>", " ")
            .replace("</strong>", " ")
            .replace("<li>", " ")
            .replace("</li>", " ")
            .replace("<ul>", " ")
            .replace("</ul>", " ")
        )

    @staticmethod
    def get_localization_data(localization: Dict[str, Dict[str, str]]) -> Localization:
        """
        Extract localization data from json file
        """
        region = None
        city = None

        if "region" in localization:
            region = localization["region"]["name"]
        elif "city" in localization:
            city = localization["city"]["name"]

        return Localization(
            region=region,
            city=city,
        )

    @staticmethod
    def get_params(params: List[Dict[str, Any]]) -> ParamsData:
        """
        Extract params data from json file
        """
        type = None
        agreement = None
        salary_from = None
        salary_to = None
        currency = None
        experience = False
        availability = None
        workplace = None

        for param in params:
            key = param["key"]
            value = param.get("value")

            if value is not None:
                if key == "type":
                    type = value["key"]
                elif key == "agreement":
                    if isinstance(value, list):
                        agreement = value[1] if len(value) > 1 else None
                    else:
                        agreement = value["key"]
                elif key == "salary":
                    if isinstance(value, list):
                        salary_from = value[0] if len(value) > 0 else None
                        salary_to = value[1] if len(value) > 1 else None
                        currency = value[3] if len(value) > 3 else None
                    else:
                        salary_from = value.get("from")
                        salary_to = value.get("to")
                        currency = value.get("currency")
                elif (
                    key == "experience"
                    and isinstance(value, list)
                    and value[0] == "exp_yes"
                ):
                    experience = True
                elif key == "availability":
                    availability = value["key"]
                elif key == "workplace":
                    workplace = value["key"]

        return ParamsData(
            type=type,
            agreement=agreement,
            salary_from=salary_from,
            salary_to=salary_to,
            currency=currency,
            experience=experience,
            availability=availability,
            workplace=workplace,
        )

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
            params_data = self.get_params(data["params"])
            localization_data = self.get_localization_data(data["location"])

            is_remote = (
                "zdalna" in params_data.workplace if params_data.workplace else False
            )
            is_hybrid = (
                "hybrid" in params_data.workplace if params_data.workplace else False
            )

            salary = Salary(
                salary_from=params_data.salary_from,
                salary_to=params_data.salary_to,
                currency=params_data.currency,
                contract_type=params_data.agreement,
                work_schedule=params_data.type,
            )

            parsed_data.append(
                ParsedOffer(
                    title=data["title"],
                    id=data["id"],
                    salary=[salary],
                    url=data["url"],
                    region=localization_data.region,
                    description=self.process_description(data["description"]),
                    remote=is_remote,
                    hybrid=is_hybrid,
                    country="PL",
                    city=localization_data.city,
                    date_created=data["created_time"],
                    date_finished=data["valid_to_time"],
                    company_name=data["user"]["name"],
                    company_logo=data["user"]["banner_mobile"],
                )
            )

        return parsed_data


def run(
    sfd: bool, spd: bool, city: str, query: str = None
) -> List[Dict[str, Any]] | None:
    result = None

    l = OLXLocalization(city)
    x = l.return_localization_data()
    olx_scraper = OLX("https://www.olx.pl/api/v1/offers/")

    if x is None:
        logging.error("Failed to scrap localization data")
    else:
        logging.info(f"Successfully scraped localization data: {x}")
        olx_scraper.set_param("city_id", str(x.city_id))
        olx_scraper.set_param("region_id", str(x.region_id))

    if query is not None:
        olx_scraper.set_param("query", "python junior")

    logging.info(f"Scraping job offers from {olx_scraper.url}")
    data = olx_scraper.fetch_data()

    if data is None:
        logging.error("Failed to scrap job offers")
    else:
        logging.info(f"Scraped {len(data)} job offers")

        if sfd:
            logging.info(f"Saving fetch data to json")
            olx_scraper.save_fetch_data_to_json(data)
            logging.info(f"Fetch data saved to json")

        result = olx_scraper.parse_offer(data)

        if result is not None:
            logging.info(f"Successfully parsed {len(result)} job offers")

            if spd:
                logging.info(f"Saving parsed data to json")
                olx_scraper.save_parsed_data_to_json(result)
                logging.info(f"Parsed data saved to json")

        else:
            logging.error("Failed to parse job offers")

    return olx_scraper.return_parsed_data(result)
