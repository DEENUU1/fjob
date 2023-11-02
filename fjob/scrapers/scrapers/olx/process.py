from ..strategy_abstract.process import Process
from ...scraper import (
    ParsedOffer,
    ParsedSalary,
    ParsedWebsite,
    ParsedLocalization,
    ParsedExperienceLevel,
    ParsedContractType,
    ParsedWorkSchedule,
)
from typing import Dict, List, Optional, Any
from .localization import Localization
from .params_data import ParamsData
from ...utils.delete_html_tags import delete_html_tags
import logging


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class OLXProcess(Process):
    def __init__(self):
        super().__init__()
        self.json_data = {}

    def parse_html(self, html) -> None:
        self.json_data = html

    @staticmethod
    def get_localization_data(localization: Dict[str, Dict[str, Any]]) -> Localization:
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

    @staticmethod
    def is_remote(text: str) -> bool:
        if not text:
            return False
        return "zdalna" in text

    @staticmethod
    def is_hybrid(text: str) -> bool:
        if not text:
            return False
        return "hybrydowa" in text

    @staticmethod
    def get_work_schedule(text: str) -> List[Optional[str]]:
        result = []
        if "fulltime" in text:
            result.append("Full time")
        elif "parttime" in text:
            result.append("Part time")
        elif "halftime":
            result.append("Temporary")

        return result

    @staticmethod
    def get_contract_type(text: str) -> List[Optional[str]]:
        result = []
        if "zlecenie" in text:
            result.append("Umowa zlecenie")
        elif "part" in text:
            result.append("Umowa o pracę")
        elif "selfemployment" in text:
            result.append("B2B")
        elif "contract" in text:
            result.append("Umowa o dzieło")

        return result

    @staticmethod
    def get_salary_schedule(text: str) -> Optional[str]:
        if not text:
            return None

        if "hourly" in text:
            return "Hourly"
        if "monthly" in text:
            return "Monthly"

    def process(self) -> List[ParsedOffer]:
        parsed_data = []
        website = ParsedWebsite(name="OLX", url="https://www.olx.pl/")

        for data in self.json_data["data"]:
            params_data = self.get_params(data["params"])
            localization_data = self.get_localization_data(data["location"])
            parsed_experience_data = self.get_experience_level(data["title"])

            exp_levels = []
            for exp in parsed_experience_data:
                exp_levels.append(ParsedExperienceLevel(name=exp))

            is_remote = self.is_remote(params_data.workplace)
            is_hybrid = self.is_hybrid(params_data.workplace)

            work_schedule = []
            work_schedule_data = self.get_work_schedule(params_data.type)
            if work_schedule_data:
                for schedule in work_schedule_data:
                    work_schedule.append(ParsedWorkSchedule(name=schedule))

            contract_types = []
            if params_data.agreement:
                for contract in params_data.agreement:
                    contract_d = self.get_contract_type(contract)
                    for d in contract_d:
                        contract_types.append(ParsedContractType(name=d))

            salary_schedule = self.get_salary_schedule(params_data.salary_schedule)
            salary_schedule_code = None
            if salary_schedule:
                if salary_schedule == "Hourly":
                    salary_schedule_code = 3
                if salary_schedule == "Monthly":
                    salary_schedule_code = 1

            salary = ParsedSalary(
                salary_from=params_data.salary_from,
                salary_to=params_data.salary_to,
                currency=params_data.currency,
                contract_type=contract_types,
                work_schedule=work_schedule,
                salary_schedule=salary_schedule_code,
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
