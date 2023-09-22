import logging
from .scraper import Scraper, ParsedOffer, Salary
from typing import Dict, List
import requests
import json

logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class JustJoinIT(Scraper):
    """
    A scraper for the JustJoin.it jobs board.
    """

    def __init__(self, url: str):
        super().__init__(url)

    def fetch_data(self) -> List[Dict[str, str]] | None:
        """
        Fetch data from JustJoin.it API.

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
            remote = data.get("workplace_type", None) == "remote"
            hybrid = data.get("employment_types", None) == "partly_remote"

            employment_types = data.get("employment_types", [{}])
            location_data = data.get("multilocation", [{}])[0]

            salary_data = []
            for salary in employment_types:
                salary_info = salary.get("salary", {})
                salary_data.append(
                    Salary(
                        salary_from=salary_info.get("from", None)
                        if salary_info
                        else None,
                        salary_to=salary_info.get("to", None) if salary_info else None,
                        currency=salary_info.get("currency", None)
                        if salary_info
                        else None,
                        contract_type=salary.get("type", None),
                    )
                )

            parsed_data.append(
                ParsedOffer(
                    title=data.get("title", None),
                    id=data.get("id", None),
                    salary=salary_data,
                    url=f"https://www.justjoin.it/offers/{data.get('id', None)}",
                    street=location_data.get("street", None),
                    remote=remote,
                    hybrid=hybrid,
                    country=data.get("country_code", None),
                    city=data.get("city", None),
                    date_created=data.get("published_at", None),
                    experience_level=data.get("experience_level", None),
                    skills=[skill["name"] for skill in data.get("skills", None)]
                    if "skills" in data
                    else None,
                    company_name=data.get("company_name", None),
                    company_logo=data.get("company_logo_url", None),
                )
            )

        return parsed_data


def run():
    c = JustJoinIT(f"https://www.justjoin.it/api/offers")

    f = c.fetch_data()
    parsed_data = c.parse_offer(f)
    if parsed_data is not None:
        logging.info(f"Successfully parsed {len(parsed_data)} job offers")
        c.save_data(parsed_data)
    else:
        logging.error("Failed to parse job offers")
