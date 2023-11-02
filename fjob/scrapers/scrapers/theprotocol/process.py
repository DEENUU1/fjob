from ..strategy_abstract.process import Process
from typing import List, Optional
from bs4 import BeautifulSoup
from ...scraper import (
    ParsedOffer,
    ParsedWebsite,
    ParsedExperienceLevel,
)


class TheProtocolProcess(Process):
    def __init__(self):
        super().__init__()
        self.parsed_data = []

    def parse_html(self, html: Optional[str]) -> None:
        soup = BeautifulSoup(html, "html.parser")
        jobs = soup.find_all("a", class_="anchorClass_a6of9et")

        for job in jobs:
            data = {}

            company_logo = None
            title = job.find("h2", class_="titleText_t1280ha4")
            company_logo_div = job.find("div", class_="companyLogo_citwoq5")
            if company_logo_div:
                company_logo = company_logo_div.find("img")
            company_name = job.find(
                "div",
                class_="rootClass_rpqnjlt body1_b1gato5c initial_i1m6fsnc textClass_t1rna8so",
            )
            skills = job.find_all("span", class_="Label_l1fs6hs4")
            work_mode = job.find("div", {"data-test": "text-workModes"})

            if title:
                data["title"] = title.text
                data["url"] = job["href"]
            if company_logo:
                data["company_logo"] = company_logo["src"]
            if company_name:
                data["company_name"] = company_name.text
            if skills:
                data["skills"] = [skill.text for skill in skills]
            if work_mode:
                data["work_mode"] = work_mode.text

            self.parsed_data.append(data)

    @staticmethod
    def is_remote(work_mode: str) -> bool:
        if "zdalna" in work_mode or "home office" in work_mode:
            return True
        return False

    @staticmethod
    def is_hybrid(work_mode: str) -> bool:
        if "hybrid" in work_mode:
            return True
        return False

    def process(self) -> List[ParsedOffer]:
        offers = []
        for data in self.parsed_data:
            is_remote, is_hybrid = False, False

            title = data.get("title")

            if not title:
                continue

            url = data.get("url")
            skills = data.get("skills")
            company_logo = data.get("company_logo")
            company_name = data.get("company_name")
            work_mode = data.get("work_mode")

            if work_mode:
                is_remote = self.is_remote(work_mode)
                is_hybrid = self.is_hybrid(work_mode)

            website = ParsedWebsite(name="TheProtocol", url="https://theprotocol.it/")

            experiences = self.get_experience_level(title)
            experiences_obj = []
            for exp in experiences:
                experiences_obj.append(ParsedExperienceLevel(name=exp))
            offer = ParsedOffer(
                title=title,
                url=f"https://theprotocol.it/{url}",
                company_logo=company_logo,
                company_name=company_name,
                skills=skills,
                is_remote=is_remote,
                is_hybrid=is_hybrid,
                experience_level=experiences_obj,
                website=website,
            )
            offers.append(offer)
        return offers
