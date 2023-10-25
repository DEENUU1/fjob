import json
import logging
from typing import Dict, List, Optional, Any
from .localization import Localization
from .params_data import ParamsData
import requests
from ...utils.get_normalized_experience_level import get_normalized_experience_level
from ...utils.get_normalized_salary_schedule import get_normalized_salary_schedule
from ...utils.delete_html_tags import delete_html_tags
from ...scraper import (
    Scraper,
    ParsedOffer,
    ParsedSalary,
    ParsedWebsite,
    ParsedLocalization,
    ParsedExperienceLevel,
)

logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class OLX(Scraper):
    """
    A scraper for the OLX jobs board.
    """

    def __init__(
        self,
        url: str = "https://www.o"
        "lx.pl/api/v1/offers?offset=0&limit=40&category_id=4&filter_refiners=spell_checker&sl=18ae25cfa80x3938008f",
    ):
        super().__init__(url)
        self.params = {
            "offset": "0",
            "sort_by": "created_at:desc",
            "limit": "50",
            "category_id": "4",
        }

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
        salary_schedule = None

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
                        salary_schedule = value.get("type")
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
            salary_schedule=salary_schedule,
        )

    def fetch_data(self) -> List[Dict[str, str]] | None:
        try:
            r = requests.get(self.url)
            r.raise_for_status()
            return json.loads(r.content)
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
        except requests.exceptions.JSONDecodeError as json_err:
            logging.error(f"JSON decoding error occurred: {json_err}")
        return None

    @staticmethod
    def get_next_page_url(json_data: Dict) -> Optional[str]:
        """
        Extract the URL for the next page
        """
        links = json_data.get("links")
        if links:
            next_page = links.get("next")
            if next_page:
                return next_page.get("href")
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
        website = ParsedWebsite(name="OLX", url="https://www.olx.pl/")

        for data in json_data["data"]:
            params_data = self.get_params(data["params"])
            localization_data = self.get_localization_data(data["location"])
            parsed_experience_data = get_normalized_experience_level(data["title"])

            exp_levels = []
            for exp in parsed_experience_data:
                exp_levels.append(ParsedExperienceLevel(name=exp))

            is_remote = (
                "zdalna" in params_data.workplace if params_data.workplace else False
            )
            is_hybrid = (
                "hybrid" in params_data.workplace if params_data.workplace else False
            )

            salary = ParsedSalary(
                salary_from=params_data.salary_from,
                salary_to=params_data.salary_to,
                currency=params_data.currency,
                contract_type=params_data.agreement,
                work_schedule=params_data.type,
                salary_schedule=get_normalized_salary_schedule(
                    params_data.salary_schedule
                ),
                type=1,
            )

            localization_object = ParsedLocalization(
                region=localization_data.region,
                city=localization_data.city,
                country="Poland",
            )

            parsed_data.append(
                ParsedOffer(
                    title=data["title"],
                    url=data["url"],
                    description=delete_html_tags(data["description"]),
                    is_remote=is_remote,
                    is_hybrid=is_hybrid,
                    experience_level=exp_levels,
                    salary=[salary],
                    website=website,
                    localizations=[localization_object],
                )
            )

        return parsed_data

    def run(self) -> None:
        while self.url:
            json_data = self.fetch_data()

            if not json_data:
                logging.error("No data received")
                break

            parsed_data = self.parse_offer(json_data)
            if not parsed_data:
                break

            self.save_data(parsed_data)
            self.url = self.get_next_page_url(json_data)
