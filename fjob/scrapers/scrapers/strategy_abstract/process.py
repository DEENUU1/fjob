from abc import abstractmethod, ABC
from typing import List, Optional, Dict, Any
from ...scraper import ParsedOffer
from offers.models import (
    Website,
    ExperienceLevel,
    Salaries,
    Localization,
    Offers,
    ContractType,
    WorkSchedule,
)
from datetime import datetime


class Process(ABC):
    def __init__(self):
        self.processed_data: List[ParsedOffer] = []

    @abstractmethod
    def parse_html(
        self, html: List[Optional[str]] | Optional[str] | Dict[str, Any]
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    def process(self) -> ParsedOffer | List[Optional[ParsedOffer]]:
        pass

    @staticmethod
    def save_to_db(parsed_offer: ParsedOffer) -> None:
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
                        ) = ContractType.objects.get_or_create(name=contract_type.name)
                        salary.contract_type.add(contract_type_obj)
                if parsed_salary.work_schedule:
                    for work_schedule in parsed_salary.work_schedule:
                        (
                            work_schedule_obj,
                            created,
                        ) = WorkSchedule.objects.get_or_create(name=work_schedule.name)
                        salary.work_schedule.add(work_schedule_obj)
                salaries.append(salary)

        localizations = []
        if parsed_offer.localizations:
            for loc in parsed_offer.localizations:
                print(loc)
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
            is_active=True,  # TODO Change that to False
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

    @staticmethod
    def get_currency(text: str) -> Optional[str]:
        currencies = ["PLN", "EUR", "USD"]
        for occurrence in currencies:
            if occurrence in text:
                return occurrence

    @staticmethod
    def get_experience_level(text: str) -> List[Optional[str]]:
        result = []
        if not text:
            return result

        text = text.lower()

        data = {
            "Intern": [
                "intern",
                "stażysta",
                "staż",
                "praktykant",
                "stażysta",
                "praktykant/stażysta",
                "praktykant / stażysta",
            ],
            "Junior": ["młodszy", "junior", "młodszy specjalista"],
            "Expert": ["ekspert", "expert"],
            "Assistant": ["asystent", "asystentka"],
            "Mid": ["mid", "regular", "specjalista (mid / regular)"],
            "Senior": ["senior", "starszy"],
            "Lead": ["lead", "kierownik", "kierownik/koordynator", "koordynator"],
            "Director": ["dyrektor", "director"],
            "Manager": ["manager", "menadżer"],
            "Worker": ["pracownik fizyczny", "worker"],
            "CEO": [
                "prezes",
            ],
        }

        for p, f in data.items():
            for x in f:
                if x in text:
                    result.append(p)

        return result
