from requests_html import HTMLSession
import logging
from .scraper import Scraper, ParsedOffer, Salary
from typing import Dict, List


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

    def fetch_data(self) -> List[Dict[str, str]]:
        """
        Scrape data from Nofluffjobs.com

        Returns:
            A list of dictionaries containing the job offer data, or None if an error occurred.
        """
        session = HTMLSession()
        offers_ls = []

        categories = [
            "backend",
            # "frontend",
            # "fullstack",
            # "mobile",
            # "embedded",
            # "artificial-intelligence",
            # "data",
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
                                "url": url,
                                "title": title_text,
                                "salary": salary_text,
                                "location": location_text,
                            }
                        )
                        new_offers_found = True

                if not new_offers_found:
                    break

                page_number += 1
                logging.info(f"Category {category} - Page {page_number} scraped")

        return offers_ls

    def parse_offer(self, json_data: List[Dict[str, str]]) -> List[ParsedOffer] | None:
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
            pass

        return parsed_data


def run():
    c = Nofluffjobs("https://nofluffjobs.com/pl/")

    f = c.fetch_data()
    logging.info(f"Successfully fetched {len(f)} job offers")
    print(f)

    # parsed_data = c.parse_offer(f)
    # if parsed_data is not None:
    #     logging.info(f"Successfully parsed {len(parsed_data)} job offers")
    #     print(parsed_data)
    #     c.save_data(parsed_data)
    # else:
    #     logging.error("Failed to parse job offers")
