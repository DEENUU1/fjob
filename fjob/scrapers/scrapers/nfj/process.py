from ..strategy_abstract.process import Process
from typing import List, Optional, Tuple
from bs4 import BeautifulSoup
from ...scraper import (
    ParsedOffer,
    ParsedSalary,
    ParsedWebsite,
    ParsedLocalization,
    ParsedExperienceLevel,
)


class NFJProcess(Process):
    def __init__(self):
        super().__init__()
        self.parsed_data = []

    def parse_html(self, html: Optional[str]) -> None:
        soup = BeautifulSoup(html, "html.parser")
        jobs = soup.find("div", class_="list-container ng-star-inserted")
        jobs_list = jobs.find_all("a", class_="posting-list-item")
        for job in jobs_list:
            data = {}
            url = job["href"]
            title = job.find(
                "h3",
                class_="posting-title__position text-truncate color-main ng-star-inserted",
            )
            company = job.find(
                "span",
                class_="d-block posting-title__company text-truncate",
            )
            company_img = job.find("img")
            salary = job.find(
                "span",
                class_="text-truncate badgy salary tw-btn tw-btn-secondary-outline tw-btn-xs ng-star-inserted",
            )
            localization = job.find(
                "span",
                class_="tw-text-ellipsis tw-inline-block tw-overflow-hidden tw-whitespace-nowrap lg:tw-max-w-[100px] tw-text-right",
            )

            if url:
                data["url"] = url
            if title:
                data["title"] = title.text
            if company:
                data["company"] = company.text
            if salary:
                data["salary"] = salary.text.replace("\xa0", "").replace("\n", "")
            if localization:
                data["localization"] = localization.text
            if company_img:
                data["company_img"] = company_img["src"]

            self.parsed_data.append(data)

    @staticmethod
    def remove_currency(salary: str) -> str:
        currencies = ["PLN", "USD", "CHF", "GBP", "EUR", "HUF", "CZK", "UAH", "BYN"]
        for currency in currencies:
            return salary.replace(currency, "")

    def process_salary(self, salary: str) -> Tuple[Optional[int], Optional[int]]:
        salary = self.remove_currency(salary)

        if "–" in salary:
            salary = salary.replace("–", "-")
            text = salary.split("-")
            num1, num2 = text
            return int(num1.replace(" ", "")), int(num2.replace(" ", ""))
        else:
            return int(salary.replace(" ", "")), None

    @staticmethod
    def is_remote(title: str, localization: str) -> bool:
        if "remote" in title.lower() or "Zdalnie" in localization:
            return True
        return False

    @staticmethod
    def is_hybrid(title: str) -> bool:
        if "hybrid" in title.lower():
            return True
        return False

    @staticmethod
    def process_localization(localization: Optional[str]) -> Optional[str]:
        pass

    def process(self) -> List[Optional[ParsedOffer]]:
        parsed_offers = []

        for pd in self.parsed_data:
            print(pd)
            title = pd.get("title")
            url = pd.get("url")
            company = pd.get("company")
            company_img = pd.get("company_img")
            salary = pd.get("salary")
            localization = pd.get("localization")

            salary_from, salary_to = self.process_salary(salary)
            is_remote = self.is_remote(title, localization)
            is_hybrid = self.is_hybrid(title)
            processed_localization = self.process_localization(localization)
            currency = self.get_currency(salary)
            experiences = self.get_experience_level(title)

            website = ParsedWebsite(name="NoFluffJobs", url="https://nofluffjobs.com/")
            localization = ParsedLocalization(city=processed_localization)
            experiences_obj = []
            for exp in experiences:
                experiences_obj.append(ParsedExperienceLevel(name=exp))
            salary = ParsedSalary(
                salary_from=salary_from,
                salary_to=salary_to,
                currency=currency,
                salary_schedule=1,
                type=2,
            )
            offer = ParsedOffer(
                title=title,
                url=f"https://nofluffjobs.com/{url}",
                company_name=company,
                company_logo=company_img,
                is_remote=is_remote,
                is_hybrid=is_hybrid,
                experience_level=experiences_obj,
                salary=[salary],
                website=website,
                localizations=[localization],
            )
            parsed_offers.append(offer)
        return parsed_offers
