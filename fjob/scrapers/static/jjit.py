from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from typing import List, Optional
from bs4 import BeautifulSoup
from ..scraper import (
    ParsedSalary,
    ParsedLocalization,
    ParsedWebsite,
    ParsedOffer,
    ParsedExperienceLevel,
    Scraper,
)
import logging

logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


BASE_URL = "https://justjoin.it/all-locations/ux"
PIXELS_TO_SCROLL = "500"


class JJIT(Scraper):
    def __init__(self, url: str = BASE_URL):
        super().__init__(url)
        self.data = []
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)

    def fetch_data(self):
        try:
            last_height = 0
            while True:
                self.extract_job_offers()
                self.driver.execute_script(f"window.scrollBy(0, {PIXELS_TO_SCROLL});")
                time.sleep(1)

                new_height = self.driver.execute_script("return window.scrollY")
                if new_height == last_height:
                    break
                last_height = new_height
        except Exception as e:
            logging.error(f"Error occurred during scraping: {e}")

    def extract_job_offers(self) -> None:
        try:
            elements = self.driver.find_elements(By.CLASS_NAME, "css-gfqoze")
            for element in elements:
                offer = {}

                soup = BeautifulSoup(element.get_attribute("innerHTML"), "html.parser")
                title_element = soup.find("h2", class_="css-r6vvd4")
                url_element = soup.find("a", class_="css-4lqp8g")
                salary_element = soup.find("div", class_="css-1qaewdq")
                skill_elements = soup.find_all("div", class_="css-1am4i4o")
                skills = [skill.text for skill in skill_elements]
                localization_element = soup.find("div", class_="css-h3r3z8")

                if title_element:
                    offer["title"] = title_element.text
                if url_element:
                    offer["url"] = url_element.get("href")
                if salary_element:
                    offer["salary"] = salary_element.text
                if skills:
                    offer["skills"] = skills
                if localization_element:
                    offer["localization"] = localization_element.text

                self.data.append(offer)
        except Exception as e:
            logging.error(f"Error occurred during extracting job offers: {e}")

    @staticmethod
    def process_salary(salary: str):
        if "Undisclosed" in salary:
            return None, None

        if "-" in salary:
            text = salary.split(" - ")
            num1, num2 = text
            return int(num1.replace(" ", "")), int(
                num2.replace(" ", "").replace("PLN", "")
            )
        else:
            return int(salary.replace("PLN", "").replace(" ", "")), None

    @staticmethod
    def get_currency(salary: str) -> Optional[str]:
        if "PLN" in salary:
            return "PLN"
        else:
            return None

    def process_skills(self, idx: int) -> None:
        skills = self.data[idx]["skills"]
        if "New" in skills:
            skills.remove("New")
        return skills

    def is_remote(self, skills: List[str], idx: int) -> bool:
        if "remote" in skills:
            self.data[idx]["skills"].remove("Fully remote")
            return True
        else:
            return False

    @staticmethod
    def is_hybrid(title: str) -> bool:
        if "hybrid" in title.lower():
            return True
        else:
            return False

    @staticmethod
    def get_experience_level(skills: List[str]) -> List[Optional[str]]:
        result = []
        skills = "".join(skills).lower()
        if "junior" in skills or "młodszy" in skills:
            result.append("Junior")
        if "intern" in skills or "internship" in skills or "stażysta" in skills:
            result.append("Internship")
        if "senior" in skills or "starszy" in skills or "expert" in skills:
            result.append("Senior")
        if "dyrektor" in skills or "direktor" in skills:
            result.append("Director")
        if "manager" in skills or "menedżer" in skills:
            result.append("Manager")

        return result

    @staticmethod
    def process_localization(localization: str) -> str:
        if ", " in localization:
            return localization.split(", ")[0]
        else:
            return localization

    def parse_offer(self, json_data=None) -> List[Optional[ParsedOffer]]:
        parsed_offer = []

        if not self.data:
            return parsed_offer

        website = ParsedWebsite(name="JustJoinIT", url="https://justjoin.it")

        try:
            for idx, offer in enumerate(self.data):
                salary_from, salary_to = self.process_salary(offer["salary"])
                currency = self.get_currency(offer["salary"])
                is_remote = self.is_remote(offer["skills"], idx)
                skills = self.process_skills(idx)
                experience_level = self.get_experience_level(offer["skills"])
                localization_data = self.process_localization(offer["localization"])
                is_hybrid = self.is_hybrid(offer["title"])

                localization = ParsedLocalization(
                    city=localization_data,
                )

                exp_levels = []
                for exp in experience_level:
                    exp_levels.append(ParsedExperienceLevel(name=exp))

                salary = ParsedSalary(
                    salary_from=salary_from,
                    salary_to=salary_to,
                    currency=currency,
                    salary_schedule="Monthly",
                    type="Netto",
                )

                parsed_offer.append(
                    ParsedOffer(
                        title=offer["title"],
                        url=f"https://justjoin.it{offer['url']}",
                        skills=skills,
                        is_remote=is_remote,
                        is_hybrid=is_hybrid,
                        experience_level=exp_levels,
                        salary=[salary],
                        website=website,
                        localizations=[localization],
                    )
                )

        except Exception as e:
            logging.error(f"Error occurred during parsing: {e}")

        logging.info(f"Parsed {len(parsed_offer)} offers from justjoin.it")
        return parsed_offer
