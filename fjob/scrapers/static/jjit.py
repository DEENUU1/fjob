from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from typing import List, Optional
from bs4 import BeautifulSoup
from ..scraper import ParsedOffer, Salary, Scraper
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

    def is_remote(self, skills: List[str], idx: int) -> bool:
        if "remote" in skills:
            self.data[idx]["skills"].remove("Fully remote")
            return True
        else:
            return False

    @staticmethod
    def get_experience_level(skills: List[str]) -> Optional[str]:
        if "Senior" in skills:
            return "senior"
        elif "Mid" in skills:
            return "mid"
        elif "Junior" in skills:
            return "junior"
        elif "Trainee" in skills:
            return "trainee"
        else:
            return None

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

        try:
            for idx, offer in enumerate(self.data):
                salary_from, salary_to = self.process_salary(offer["salary"])
                currency = self.get_currency(offer["salary"])
                is_remote = self.is_remote(offer["skills"], idx)
                skills = self.process_skills(idx)
                experience_level = self.get_experience_level(offer["skills"])
                localization = self.process_localization(offer["localization"])

                salary = Salary(
                    salary_from=salary_from,
                    salary_to=salary_to,
                    currency=currency,
                )

                parsed_offer.append(
                    ParsedOffer(
                        title=offer["title"],
                        id=offer["url"],
                        url=f"https://justjoin.it{offer['url']}",
                        salary=[salary],
                        city=localization,
                        remote=is_remote,
                        experience_level=experience_level if experience_level else None,
                        skills=skills,
                    )
                )

        except Exception as e:
            logging.error(f"Error occurred during parsing: {e}")

        logging.info(f"Parsed {len(parsed_offer)} offers from justjoin.it")
        return parsed_offer
