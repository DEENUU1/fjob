from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from typing import List, Dict, Any
from bs4 import BeautifulSoup
from ..scraper import ParsedOffer, Salary, Scraper


BASE_URL = "https://justjoin.it/all-locations/ux"
PIXELS_TO_SCROLL = "500"
driver = webdriver.Chrome()
driver.get(BASE_URL)


class JJIT(Scraper):
    def __init__(self, url: str = BASE_URL):
        super().__init__(url)
        self.data = []

    def fetch_data(self):
        try:
            last_height = 0
            while True:
                self.extract_job_offers()
                driver.execute_script(f"window.scrollBy(0, {PIXELS_TO_SCROLL});")
                time.sleep(1)

                new_height = driver.execute_script("return window.scrollY")
                if new_height == last_height:
                    break
                last_height = new_height
        except Exception as e:
            print(e)

    def extract_job_offers(self) -> None:
        try:
            elements = driver.find_elements(By.CLASS_NAME, "css-gfqoze")
            for element in elements:
                offer = {}

                soup = BeautifulSoup(element.get_attribute("innerHTML"), "html.parser")
                title_element = soup.find("h2", class_="css-r6vvd4")
                url_element = soup.find("a", class_="css-4lqp8g")
                salary_element = soup.find("div", class_="css-1qaewdq")
                skill_elements = soup.find_all("div", class_="css-1am4i4o")
                skills = [skill.text for skill in skill_elements]
                if title_element:
                    offer["title"] = title_element.text
                if url_element:
                    offer["url"] = url_element.get("href")
                if salary_element:
                    offer["salary"] = salary_element.text
                if skills:
                    offer["skills"] = skills

                self.data.append(offer)
        except Exception as e:
            print(e)

    def parse_offer(self, json_data=None) -> List[ParsedOffer]:
        parsed_offer = []
        for offer in self.data:
            parsed_offer.append(
                ParsedOffer(
                    title=offer["title"],
                    url=offer["url"],
                    salary=...,
                    city=...,
                    remote=...,
                    hybrid=...,
                    experience_level=...,
                    skills=...,
                    company_name=...,
                    company_logo=...,
                )
            )

        return parsed_offer
