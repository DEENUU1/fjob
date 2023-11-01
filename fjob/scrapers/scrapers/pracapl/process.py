from ..strategy_abstract.process import Process
from typing import List, Optional, Any, Dict
from bs4 import BeautifulSoup
from ...scraper import (
    ParsedOffer,
    ParsedSalary,
    ParsedWebsite,
    ParsedLocalization,
    ParsedExperienceLevel,
    ParsedContractType,
    ParsedWorkSchedule,
)


class PracaPLProcess(Process):
    def __init__(self):
        super().__init__()
        self.parsed_data = []

    def parse_html(self, html: Optional[str]) -> None:
        soup = BeautifulSoup(html, "html.parser")
        jobs = soup.find_all("li", class_="listing__item")

        for job in jobs:
            data = {}

            title = job.find("a", class_="listing__title")
            company_logo_div = job.find("div", class_="listing__logo-block")
            company_logo = company_logo_div.find("img")
            company_name = job.find("a", class_="listing__employer-name")
            localization = job.find("span", class_="listing__location-name")
            work_model = job.find("span", class_="listing__work-model--house-window")
            additional_info_div = job.find("div", class_="listing__main-details")

            if title:
                data["title"] = title.text
                data["url"] = title["href"]
            if company_logo:
                data["company_logo"] = company_logo["src"]
            if company_name:
                data["company_name"] = company_name.text
            if localization:
                data["localization"] = localization.text.replace("\xa0", "")
            if additional_info_div:
                data["info"] = additional_info_div.text
            if work_model:
                data["work_model"] = [work_model.text]
            self.parsed_data.append(data)

    @staticmethod
    def is_remote(text: str) -> bool:
        return "zdalna" in text

    @staticmethod
    def is_hybrid(text: str) -> bool:
        return "hybrydowa" in text

    @staticmethod
    def process_localization(localization: Optional[str]) -> Dict[str, Any]:
        result = {}
        localization = localization.split("\n")
        first_ele = localization[0]
        if first_ele[0].islower():
            result["region"] = localization[0]
        if first_ele[0].isupper():
            result["city"] = localization[0]
        return result

    @staticmethod
    def get_work_schedule(text: str) -> List[Optional[str]]:
        result = []
        if "pełny etat" in text:
            result.append("Full time")
        elif "część etatu" in text:
            result.append("Part time")
        elif "tymczasowa/dodatkowa":
            result.append("Temporary")

        return result

    @staticmethod
    def get_contract_type(text: str) -> List[Optional[str]]:
        result = []
        if "umowa o prace" in text:
            result.append("Umowa o pracę")
        elif "umowa o dzieło" in text:
            result.append("Umowa o dzieło")
        elif "umowa zlecenie" in text:
            result.append("Umowa zlecenie")
        elif "kontrakt B2B" in text:
            result.append("B2B")
        elif "umowa o pracę tymczasową" in text:
            result.append("Umowa o pracę tymczasową")
        elif "umowa agencyjna" in text:
            result.append("Umowa agencyjna")
        elif "umowa o staż/praktykę" in text:
            result.append("Umowa o staż/praktykę")
        elif "umowa o zastępstwo" in text:
            result.append("Umowa o zastępstwo")

        return result

    def process(self) -> List[ParsedOffer]:
        offers = []
        is_remote = False
        is_hybrid = False

        for data in self.parsed_data:
            title = data.get("title")
            url = data.get("url")
            work_mode = data.get("work_model")
            localization = data.get("localization")
            company_logo = data.get("company_logo")
            company_name = data.get("company_name")
            info = data.get("info")

            if work_mode:
                is_remote = self.is_remote(work_mode)
                is_hybrid = self.is_hybrid(work_mode)
            if localization:
                processed_localization = self.process_localization(localization)
                localization = ParsedLocalization(
                    city=processed_localization.get("city"),
                    region=processed_localization.get("region"),
                )
            currency = self.get_currency(info)
            experiences = self.get_experience_level(info)
            website = ParsedWebsite(name="PracaPL", url="https://www.praca.pl/")

            experiences_obj = []
            if experiences:
                for exp in experiences:
                    experiences_obj.append(ParsedExperienceLevel(name=exp))

            workschedule = self.get_work_schedule(info)
            workschedule_obj = []
            if workschedule:
                for schedule in workschedule:
                    workschedule_obj.append(ParsedWorkSchedule(name=schedule))

            contract_types = self.get_contract_type(info)
            contracts = []
            if contract_types:
                for contract in contract_types:
                    contracts.append(ParsedContractType(name=contract))

            salary = ParsedSalary(
                contract_type=contracts,
                work_schedule=workschedule_obj,
                currency=currency,
            )

            offer = ParsedOffer(
                title=title,
                url=url,
                company_logo=company_logo,
                company_name=company_name,
                is_remote=is_remote,
                is_hybrid=is_hybrid,
                experience_level=experiences_obj,
                salary=[salary],
                website=website,
                localizations=[localization],
            )
            offers.append(offer)
        return offers
