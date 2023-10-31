from ..strategy_abstract.process import Process
from typing import List, Optional, Dict, Any
from bs4 import BeautifulSoup
from ...scraper import ParsedOffer


class JJITProcess(Process):
    def __init__(self):
        super().__init__()

    def parse_html(self, html: Optional[str]) -> Dict[str, Any]:
        soup = BeautifulSoup(html, "html.parser")
        parsed_data = {}

        title_element = soup.find("h2", class_="css-16gpjqw")
        url_element = soup.find("a", class_="css-4lqp8g")
        salary_element = soup.find("div", class_="css-1qaewdq")
        skill_elements = soup.find_all("div", class_="css-1am4i4o")
        skills = [skill.text for skill in skill_elements]
        localization_element = soup.find("div", class_="css-h3r3z8")

        if title_element:
            parsed_data["title"] = title_element.text
        if url_element:
            parsed_data["url"] = url_element["href"]
        if salary_element:
            parsed_data["salary"] = salary_element.text
        if skills:
            parsed_data["skills"] = skills
        if localization_element:
            parsed_data["localization"] = localization_element.text

        return parsed_data

    def clean_data(self) -> None:
        pass

    def normalize(self) -> None:
        pass
