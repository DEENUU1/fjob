from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Optional, Any

from offers.models import offers, salaries
import logging
from django.db import transaction


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@dataclass
class Salary:
    salary_from: Optional[int] = None
    salary_to: Optional[int] = None
    currency: Optional[str] = None
    contract_type: Optional[str] = None
    work_schedule: Optional[str] = None


@dataclass
class ParsedOffer:
    title: Optional[str] = None
    id: Optional[str] = None
    salary: Optional[List[Salary]] = None
    url: Optional[str] = None
    street: Optional[str] = None
    region: Optional[str] = None
    additional_data: Optional[Dict[str, str]] = None
    description: Optional[str] = None
    remote: Optional[bool] = None
    hybrid: Optional[bool] = None
    country: Optional[str] = None
    city: Optional[str] = None
    date_created: Optional[str] = None
    date_finished: Optional[str] = None
    experience_level: Optional[str] = None
    skills: Optional[List[str]] = None
    company_name: Optional[str] = None
    company_logo: Optional[str] = None


class Scraper(ABC):
    def __init__(self, url: str, search: Dict[str, str] = None):
        self.url = url
        self.search = search

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
    def save_data(data_list: List[ParsedOffer]) -> None:
        try:
            with transaction.atomic():
                for parsed_offer in data_list:
                    existing_offer = offers.Offers.objects.filter(
                        url=parsed_offer.url
                    ).first()
                    if existing_offer:
                        continue

                    offer = offers.Offers(
                        title=parsed_offer.title,
                        url=parsed_offer.url,
                        street=parsed_offer.street,
                        region=parsed_offer.region,
                        additional_data=parsed_offer.additional_data,
                        description=parsed_offer.description,
                        remote=parsed_offer.remote,
                        hybrid=parsed_offer.hybrid,
                        country=parsed_offer.country,
                        city=parsed_offer.city,
                        date_created=parsed_offer.date_created,
                        date_finished=parsed_offer.date_finished,
                        experience_level=parsed_offer.experience_level,
                        company_name=parsed_offer.company_name,
                        company_logo=parsed_offer.company_logo,
                    )
                    offer.save()

                    if parsed_offer.salary:
                        for parsed_salary in parsed_offer.salary:
                            salary = salaries.Salaries(
                                salary_from=parsed_salary.salary_from,
                                salary_to=parsed_salary.salary_to,
                                currency=parsed_salary.currency,
                                contract_type=parsed_salary.contract_type,
                                work_schedule=parsed_salary.work_schedule,
                            )
                            salary.offer = offer
                            salary.save()
            logging.info(f"Saved scraped data to database")
        except Exception as e:
            logging.error(f"Error occurred while saving data to database: {e}")
