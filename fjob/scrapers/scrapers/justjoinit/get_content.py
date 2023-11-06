from ..strategy_abstract.get_content import GetContentStrategy
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

CATEGORIES = [
    "javascript",
    "html",
    "php",
    "ruby",
    "java",
    "net",
    "scala",
    "c",
    "mobile",
    "testing",
    "devops",
    "admin",
    "ux",
    "pm",
    "game",
    "analytics",
    "security",
    "data",
    "go",
    "support",
    "erp",
    "architecture",
    "other",
]


class GetJustJoinITContent(GetContentStrategy):
    def __init__(self, category: str):
        super().__init__(
            website="JustJoinIT",
            base_url=f"https://justjoin.it/all-locations/{category}",
        )
        self.category = category
        self.pixels_to_scroll = "500"
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)

    def fetch_content(self) -> None:
        try:
            last_height = 0
            while True:
                elements = self.driver.find_elements(By.CLASS_NAME, "css-gpb9dg")
                if elements:
                    for element in elements:
                        self.data.append(element.get_attribute("outerHTML"))
                self.driver.execute_script(
                    f"window.scrollBy(0, {self.pixels_to_scroll});"
                )
                time.sleep(1)

                new_height = self.driver.execute_script("return window.scrollY")
                if new_height == last_height:
                    break
                last_height = new_height
                logging.info(f"Fetched content from {self.website} - {self.base_url}")

        except Exception as e:
            logging.error(f"Error while fetching content from {self.website}")
