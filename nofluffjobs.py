from requests_html import HTMLSession
from dataclasses import dataclass
from typing import Optional


@dataclass
class Data:
    url: Optional[str] = None
    title: Optional[str] = None
    salary: Optional[str] = None
    location: Optional[str] = None


session = HTMLSession()
offers_ls = []

base_url = "https://nofluffjobs.com/pl/"

categories = [
    "backend",
    "frontend",
    "fullstack",
    "mobile",
    "embedded",
    "artificial-intelligence",
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

for category in categories:
    page_number = 1

    while True:
        url = f"{base_url}{category}?page={page_number}"
        r = session.get(url)
        r.html.render()
        offers = r.html.find("div.list-container.ng-star-inserted a")
        new_offers_found = False

        for offer in offers:
            url = offer.attrs["href"]

            title_selector = offer.find("h3.posting-title__position", first=True)
            title_text = title_selector.text.strip() if title_selector else None

            salary_selector = offer.find("span.text-truncate.badgy.salary", first=True)
            salary_text = salary_selector.text.strip() if salary_selector else None

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
                    Data(
                        url=url,
                        title=title_text,
                        salary=salary_text,
                        location=location_text,
                    )
                )
                new_offers_found = True

        if not new_offers_found:
            break

        page_number += 1
        print(f"Category: {category}, Page: {page_number}")

print(offers_ls)
print(f"Offers: {len(offers_ls)}")
