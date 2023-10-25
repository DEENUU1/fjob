from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any
import json
from django.db import transaction
from offers.models import (
    Website,
    ExperienceLevel,
    Salaries,
    Localization,
    Offers,
    ContractType,
    WorkSchedule,
)
import logging
from datetime import datetime


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@dataclass
class ParsedWebsite:
    name: str
    url: Optional[str] = None


@dataclass
class ParsedWorkSchedule:
    name: str


@dataclass
class ParsedContractType:
    name: str


@dataclass
class ParsedExperienceLevel:
    name: str


@dataclass
class ParsedSalary:
    salary_from: Optional[int] = None
    salary_to: Optional[int] = None
    currency: Optional[str] = None
    contract_type: List[Optional[ParsedContractType]] = None
    work_schedule: List[Optional[ParsedWorkSchedule]] = None
    salary_schedule: Optional[int] = None
    type: Optional[int] = None


@dataclass
class ParsedLocalization:
    country: Optional[str] = None
    city: Optional[str] = None
    region: Optional[str] = None
    street: Optional[str] = None


@dataclass
class ParsedOffer:
    title: Optional[str] = None
    url: Optional[str] = None
    description: Optional[str] = None
    skills: Optional[List[str]] = None
    company_name: Optional[str] = None
    company_logo: Optional[str] = None
    is_remote: Optional[bool] = False
    is_hybrid: Optional[bool] = False
    is_active: Optional[bool] = True
    is_promoted: Optional[bool] = False
    date_created: Optional[str] = None
    date_finished: Optional[str] = None
    experience_level: Optional[List[ParsedExperienceLevel]] = None
    salary: Optional[List[ParsedSalary]] = None
    website: Optional[ParsedWebsite] = None
    localizations: Optional[List[ParsedLocalization]] = None


class Scraper(ABC):
    def __init__(self, url: str, search: Dict[str, str] = None):
        self.url = url
        self.search = search

    @staticmethod
    def save_to_json(data: List[Optional[ParsedOffer]], filename: str) -> None:
        offers_data = []
        for offer in data:
            offer_data = asdict(offer)
            offers_data.append(offer_data)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(offers_data, f, ensure_ascii=False, indent=4)

    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def parse_offer(self, data):
        pass

    @staticmethod
    def return_parsed_data(parsed_data: List[ParsedOffer]) -> List[Dict[str, Any]]:
        return [offer.__dict__ for offer in parsed_data]

    @staticmethod
    def save_data(parsed_offers: List[ParsedOffer]) -> None:
        for parsed_offer in parsed_offers:
            website, created = Website.objects.get_or_create(
                name=parsed_offer.website.name,
                url=parsed_offer.website.url,
            )

            experience_levels = []
            if parsed_offer.experience_level:
                for exp_level in parsed_offer.experience_level:
                    level, created = ExperienceLevel.objects.get_or_create(
                        name=exp_level.name
                    )
                    experience_levels.append(level)

            salaries = []
            if parsed_offer.salary:
                for parsed_salary in parsed_offer.salary:
                    salary = Salaries(
                        salary_from=parsed_salary.salary_from,
                        salary_to=parsed_salary.salary_to,
                        currency=parsed_salary.currency,
                        salary_schedule=parsed_salary.salary_schedule,
                        type=parsed_salary.type,
                    )
                    salary.save()
                    if parsed_salary.contract_type:
                        for contract_type in parsed_salary.contract_type:
                            (
                                contract_type_obj,
                                created,
                            ) = ContractType.objects.get_or_create(
                                name=contract_type.name
                            )
                            salary.contract_type.add(contract_type_obj)
                    if parsed_salary.work_schedule:
                        for work_schedule in parsed_salary.work_schedule:
                            (
                                work_schedule_obj,
                                created,
                            ) = WorkSchedule.objects.get_or_create(
                                name=work_schedule.name
                            )
                            salary.work_schedule.add(work_schedule_obj)
                    salaries.append(salary)

            localizations = []
            if parsed_offer.localizations:
                for loc in parsed_offer.localizations:
                    localization = Localization(
                        country=loc.country,
                        city=loc.city,
                        region=loc.region,
                        street=loc.street,
                    )
                    localization.save()
                    localizations.append(localization)

            offer = Offers(
                title=parsed_offer.title,
                url=parsed_offer.url,
                description=parsed_offer.description,
                skills=", ".join(parsed_offer.skills) if parsed_offer.skills else None,
                company_name=parsed_offer.company_name,
                company_logo=parsed_offer.company_logo,
                is_remote=parsed_offer.is_remote,
                is_hybrid=parsed_offer.is_hybrid,
                is_active=parsed_offer.is_active,
                date_created=datetime.strptime(parsed_offer.date_created, "%Y-%m-%d")
                if parsed_offer.date_created
                else None,
                date_finished=datetime.strptime(parsed_offer.date_finished, "%Y-%m-%d")
                if parsed_offer.date_finished
                else None,
                website=website,
            )
            offer.save()
            offer.experience_level.set(experience_levels)
            offer.salary.set(salaries)
            offer.localizations.set(localizations)
