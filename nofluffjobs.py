from requests_html import HTMLSession
from dataclasses import dataclass
from typing import Optional


@dataclass
class Data:
    url: Optional[str] = None
    title: Optional[str] = None
    salary: Optional[str] = None
    location: Optional[str] = None


page_number = 1
session = HTMLSession()
offers_ls = []


urls = {
    "backend": "https://nofluffjobs.com/pl/backend",
    "frontend": "https://nofluffjobs.com/pl/frontend",
    "fullstack": "https://nofluffjobs.com/pl/fullstack",
    "mobile": "https://nofluffjobs.com/pl/mobile",
    "embedded": "https://nofluffjobs.com/pl/embedded",
    "ai": "https://nofluffjobs.com/pl/artificial-intelligence",
    "data": "https://nofluffjobs.com/pl/data",
    "business-intelligence": "https://nofluffjobs.com/pl/business-intelligence",
    "business-analyst": "https://nofluffjobs.com/pl/business-analyst",
    "product-management": "https://nofluffjobs.com/pl/product-management",
    "testing": "https://nofluffjobs.com/pl/testing",
    "devops": "https://nofluffjobs.com/pl/devops",
    "sys-administrator": "https://nofluffjobs.com/pl/sys-administrator",
    "security": "https://nofluffjobs.com/pl/security",
    "architecture": "https://nofluffjobs.com/pl/architecture",
    "game-dev": "https://nofluffjobs.com/pl/game-dev",
    "project-manager": "https://nofluffjobs.com/pl/project-manager",
    "agile": "https://nofluffjobs.com/pl/agile",
    "design": "https://nofluffjobs.com/pl/design",
    "support": "https://nofluffjobs.com/pl/support",
    "erp": "https://nofluffjobs.com/pl/erp",
    "other": "https://nofluffjobs.com/pl/other",
    "hr": "https://nofluffjobs.com/pl/hr",
    "marketing": "https://nofluffjobs.com/pl/marketing",
    "sales": "https://nofluffjobs.com/pl/sales",
    "finance": "https://nofluffjobs.com/pl/finance",
    "office-administration": "https://nofluffjobs.com/pl/office-administration",
    "consulting": "https://nofluffjobs.com/pl/consulting",
    "customer-service": "https://nofluffjobs.com/pl/customer-service",
}


while True:
    url = f"https://nofluffjobs.com/pl/backend?page={page_number}"
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
        location_text = location_selector.text.strip() if location_selector else None

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
    print(page_number)

print(offers_ls)
print(f"Offers: {len(offers_ls)}")
