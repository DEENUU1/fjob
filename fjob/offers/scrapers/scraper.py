from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from dataclasses import dataclass
from offers.models import Offers, Salaries
from django.db import transaction


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
    def parse_offer(self, json_data: List[Dict[str, str]]):
        pass

    @transaction.atomic()
    def save_data(self, data_list: List[ParsedOffer]):
        """
        Save parsed data to database.

        :param data_list: List of parsed data.
        :return: List of saved data.
        :rtype: List[Offers]

        """

        saved_offers = []

        for parsed_offer in data_list:
            try:
                offer = Offers.objects.get(url=parsed_offer.url)
            except Offers.DoesNotExist:
                offer = Offers(url=parsed_offer.url)

            offer.title = parsed_offer.title
            offer.url = parsed_offer.url
            offer.street = parsed_offer.street
            offer.region = parsed_offer.region
            offer.additional_data = parsed_offer.additional_data
            offer.description = parsed_offer.description
            offer.remote = parsed_offer.remote
            offer.hybrid = parsed_offer.hybrid
            offer.country = parsed_offer.country
            offer.city = parsed_offer.city
            offer.date_created = parsed_offer.date_created
            offer.date_finished = parsed_offer.date_finished
            offer.experience_level = parsed_offer.experience_level
            offer.skills = parsed_offer.skills
            offer.company_name = parsed_offer.company_name
            offer.company_logo = parsed_offer.company_logo

            offer.save()

            if parsed_offer.salary:
                for salary_data in parsed_offer.salary:
                    salary = Salaries(
                        salary_from=salary_data.salary_from,
                        salary_to=salary_data.salary_to,
                        currency=salary_data.currency,
                        contract_type=salary_data.contract_type,
                        work_schedule=salary_data.work_schedule,
                    )
                    salary.save()
                    offer.salary.add(salary)

            saved_offers.append(offer)

        return saved_offers
