from requests_html import HTMLSession
import logging
from .scraper import Scraper, ParsedOffer, Salary
from typing import Dict, List, Any
import re

logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Nofluffjobs(Scraper):
    """
    A scraper for the nofluffjobs.com jobs board.
    """

    def __init__(self, url: str):
        super().__init__(url)

    @staticmethod
    def parse_salary(salary_text: str) -> Salary:
        """
        Parse a salary data to return Salary dataclass object
        """
        pattern_1 = r"(\d+)\s*–\s*(\d+)\s*PLN$"
        pattern_2 = r"(\d+)\s+([A-Z]+)"
        match = re.search(pattern_1, salary_text)
        match2 = re.search(pattern_2, salary_text)

        if not match2:
            pass
        else:
            num = match.group(1)
            currency = match2.group(2)
            return Salary(
                salary_from=int(num),
                currency=currency,
            )

        if not match:
            pass
        else:
            first_num = match.group(1).replace("\xa0", "")
            second_num = match.group(2).replace("\xa0", "")
            currency = match.group(3)

            return Salary(
                salary_from=int(first_num),
                salary_to=int(second_num),
                currency=currency,
            )

    @staticmethod
    def check_for_experience_status_in_title(title: str) -> str | None:
        """
        Check if experience status (junior, mid, senior) is included in the title.
        """
        title.lower()
        result = None
        if "intern" in title:
            result = "intern"
        if "junior" in title:
            result = "junior"
        elif "mid" in title:
            result = "mid"
        elif "senior" in title:
            result = "senior"
        return result

    @staticmethod
    def is_remote(localization: str) -> bool:
        """
        Check if 'Zdalnie' is in localization.
        """
        return "Zdalnie" in localization

    def fetch_data(self) -> List[Dict[str, str]]:
        """
        Scrape data from Nofluffjobs.com

        Returns:
            A list of dictionaries containing the job offer data, or None if an error occurred.
        """
        session = HTMLSession()
        offers_ls = []

        categories = [
            # "backend",
            # "frontend",
            # "fullstack",
            # "mobile",
            # "embedded",
            # "artificial-intelligence",
            "data",
            # "business-intelligence",
            # "business-analyst",
            # "product-management",
            # "testing",
            # "devops",
            # "sys-administrator",
            # "security",
            # "architecture",
            # "game-dev",
            # "project-manager",
            # "agile",
            # "design",
            # "support",
            # "erp",
            # "other",
            # "hr",
            # "marketing",
            # "sales",
            # "finance",
            # "office-administration",
            # "consulting",
            # "customer-service",
        ]

        for category in categories:
            page_number = 1

            while True:
                url = f"{self.url}{category}?page={page_number}"
                r = session.get(url)
                r.html.render()
                offers = r.html.find("div.list-container.ng-star-inserted a")
                new_offers_found = False

                for offer in offers:
                    url = offer.attrs["href"]

                    title_selector = offer.find(
                        "h3.posting-title__position", first=True
                    )
                    title_text = title_selector.text.strip() if title_selector else None

                    salary_selector = offer.find(
                        "span.text-truncate.badgy.salary", first=True
                    )
                    salary_text = (
                        salary_selector.text.strip() if salary_selector else None
                    )

                    location_selector = offer.find("span.tw-text-ellipsis", first=True)
                    location_text = (
                        location_selector.text.strip() if location_selector else None
                    )

                    if (
                        title_text is not None
                        and salary_text is not None
                        and location_text is not None
                    ):
                        offers_ls.append(
                            {
                                "id": url,
                                "title": title_text,
                                "salary": salary_text,
                                "location": location_text,
                                "experience_level": self.check_for_experience_status_in_title(
                                    title_text
                                ),
                                "is_remote": self.is_remote(location_text),
                            }
                        )
                        new_offers_found = True

                if not new_offers_found:
                    break

                page_number += 1
                logging.info(f"Category {category} - Page {page_number} scraped")

        return offers_ls

    def parse_offer(self, json_data: List[Dict[str, Any]]) -> List[ParsedOffer] | None:
        """
        Parse fetched data and return a list of ParsedOffer objects.

        Args:
            json_data: A list of dictionaries containing the job offer data.

        Returns:
            A list of ParsedOffer objects, or None if an error occurred.
        """

        if not json_data:
            logging.warning("No data received")
            return None

        parsed_data = []
        for data in json_data:
            salary = self.parse_salary(data["salary"])
            parsed_obj = ParsedOffer(
                title=data["title"],
                id=data["id"],
                url=f"https://nofluffjobs.com/pl/{data['id']}",
                salary=[salary],
                city=data["location"],
                experience_level=data["experience_level"],
                remote=data["is_remote"],
            )
            parsed_data.append(parsed_obj)

        return parsed_data


def run():
    c = Nofluffjobs("https://nofluffjobs.com/pl/")

    f = c.fetch_data()
    logging.info(f"Successfully fetched {len(f)} job offers")
    print(f)

    parsed_data = c.parse_offer(f)
    if parsed_data is not None:
        logging.info(f"Successfully parsed {len(parsed_data)} job offers")
        print(parsed_data)
        c.save_data(parsed_data)
    else:
        logging.error("Failed to parse job offers")
