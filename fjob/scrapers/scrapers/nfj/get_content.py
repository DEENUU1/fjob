from ..strategy_abstract.get_content import GetContentStrategy
import logging
from selenium import webdriver
from bs4 import BeautifulSoup


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

categories = [
    "backend",
    "frontend",
    "fullstack",
    "mobile",
    "embedded",
    "artificial-intelligence",
    "data",
    "data",
    "business-intelligence",
    "business-analyst",
    "product-management",
    "testing",
    "devops",
    "sys-administrator",
    "security",
    "architecture",
    "game-dev",
    "project-manager",
    "agile",
    "design",
    "support",
    "erp",
    "other",
    "hr",
    "marketing",
    "sales",
    "finance",
    "office-administration",
    "consulting",
    "customer-service",
]


class GetNFJContent(GetContentStrategy):
    def __init__(self):
        super().__init__(website="NFJ", base_url="https://nofluffjobs.com/pl")
        self.driver = webdriver.Chrome()

    def fetch_content(self) -> None:
        for category in categories:
            page = 1

            while True:
                url = f"{self.base_url}/{category}?page={page}"
                try:
                    self.driver.get(url)
                    content = self.driver.page_source

                    soup = BeautifulSoup(content, "html.parser")
                    jobs = soup.find("div", class_="list-container ng-star-inserted")
                    a_tag = soup.find("a")
                    if not a_tag:
                        break

                    if not jobs:
                        break

                    self.data.append(content)
                    page += 1
                except Exception as e:
                    logging.error(f"Failed to fetch content from {url}: {e}")

        self.driver.quit()
