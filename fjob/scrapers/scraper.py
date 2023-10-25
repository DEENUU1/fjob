from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Any
import json

from offers.models import Website, ExperienceLevel, Salaries, Localization, Offers
import logging
from django.db import transaction
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
class ParsedExperienceLevel:
    name: str


@dataclass
class ParsedSalary:
    salary_from: Optional[int] = None
    salary_to: Optional[int] = None
    currency: Optional[str] = None
    contract_type: Optional[str] = None
    work_schedule: Optional[str] = None
    salary_schedule: Optional[str] = None
    type: Optional[str] = None


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
            if parsed_offer.website:
                website_obj, _ = Website.objects.get_or_create(
                    name=parsed_offer.website.name
                )
            else:
                website_obj = None

            experience_levels = []
            if parsed_offer.experience_level:
                for level in parsed_offer.experience_level:
                    experience_level, _ = ExperienceLevel.objects.get_or_create(
                        name=level.name
                    )
                    experience_levels.append(experience_level)

            salaries = []
            if parsed_offer.salary:
                for salary in parsed_offer.salary:
                    s = Salaries(
                        salary_from=salary.salary_from,
                        salary_to=salary.salary_to,
                        currency=salary.currency,
                        contract_type=salary.contract_type,
                        work_schedule=salary.work_schedule,
                        # salary_schedule=salary.salary_schedule,
                        # type=salary.type,
                    )
                    s.save()
                    salaries.append(s)

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
                skills=",".join(parsed_offer.skills) if parsed_offer.skills else "",
                company_name=parsed_offer.company_name,
                company_logo=parsed_offer.company_logo,
                is_remote=parsed_offer.is_remote,
                is_hybrid=parsed_offer.is_hybrid,
                is_active=parsed_offer.is_active,
                is_promoted=parsed_offer.is_promoted,
                date_created=datetime.strptime(parsed_offer.date_created, "%Y-%m-%d")
                if parsed_offer.date_created
                else None,
                date_finished=datetime.strptime(parsed_offer.date_finished, "%Y-%m-%d")
                if parsed_offer.date_finished
                else None,
                website=website_obj,
            )
            offer.save()

            for level in experience_levels:
                offer.experience_level.add(level)

            for salary in salaries:
                offer.salary.add(salary)

            for loc in localizations:
                offer.localizations.add(loc)
