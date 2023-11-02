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


class JJITProcess(Process):
    def __init__(self):
        super().__init__()
        self.parsed_data = {}

    def parse_html(self, html: Optional[str]) -> None:
        soup = BeautifulSoup(html, "html.parser")

        title_element = soup.find("h2", class_="css-16gpjqw")
        url_element = soup.find("a", class_="css-4lqp8g")
        salary_element = soup.find("div", class_="css-1qaewdq")
        skill_elements = soup.find_all("div", class_="css-1am4i4o")
        skills = [skill.text for skill in skill_elements]
        localization_element = soup.find("div", class_="css-h3r3z8")
        company_logo_div = soup.find("div", class_="css-xlz5cy")
        company_logo = company_logo_div.find("img")
        company_name_div = soup.find("div", class_="css-fmb6qw")
        company_name = company_name_div.find("span")

        if title_element:
            self.parsed_data["title"] = title_element.text
        if url_element:
            self.parsed_data["url"] = url_element["href"]
        if salary_element:
            self.parsed_data["salary"] = salary_element.text
        if skills:
            self.parsed_data["skills"] = skills
        if localization_element:
            self.parsed_data["localization"] = localization_element.text
        if company_logo:
            self.parsed_data["company_logo"] = company_logo["src"]
        if company_name:
            self.parsed_data["company_name"] = company_name.text

    @staticmethod
    def process_salary(salary: str) -> Tuple[Optional[int], Optional[int]]:
        if "Undisclosed" in salary:
            return None, None
        salary = salary.replace("PLN", "")

        if "-" in salary:
            text = salary.split("-")
            num1, num2 = text
            return int(num1.replace(" ", "")), int(num2.replace(" ", ""))
        else:
            return int(salary.replace(" ", "")), None

    @staticmethod
    def process_skills(skills: List[str]) -> List[str]:
        to_delete = ["New", "Fully remote"]
        return [element for element in skills if element not in to_delete]

    @staticmethod
    def is_remote(skills: List[str], title: str) -> bool:
        if "remote" in skills or "remote" in title.lower():
            return True
        return False

    @staticmethod
    def is_hybrid(title: str) -> bool:
        if "hybrid" in title.lower():
            return True
        return False

    @staticmethod
    def process_localization(localization: Optional[str]) -> Optional[str]:
        if not localization:
            return None
        if ", " in localization:
            return localization.split(", ")[0]
        else:
            return localization

    def process(self) -> ParsedOffer:
        title = self.parsed_data.get("title")
        url = self.parsed_data.get("url")
        salary = self.parsed_data.get("salary")
        skills = self.parsed_data.get("skills")
        localization = self.parsed_data.get("localization")
        company_logo = self.parsed_data.get("company_logo")
        company_name = self.parsed_data.get("company_name")

        salary_from, salary_to = self.process_salary(salary)
        is_remote = self.is_remote(skills, title)
        is_hybrid = self.is_hybrid(title)
        processed_skills = self.process_skills(skills)
        processed_localization = self.process_localization(localization)
        currency = self.get_currency(salary)
        experiences = self.get_experience_level(title)
        website = ParsedWebsite(name="JustJoinIT", url="https://justjoin.it/")
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
            url=f"https://justjoin.it{url}",
            skills=processed_skills,
            company_logo=company_logo,
            company_name=company_name,
            is_remote=is_remote,
            is_hybrid=is_hybrid,
            experience_level=experiences_obj,
            salary=[salary],
            website=website,
            localizations=[localization],
        )
        return offer
