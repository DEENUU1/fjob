from selenium import webdriver
from bs4 import BeautifulSoup
import time
from ..chrome_driver import chrome_driver_configuration


BASE_URL = "https://nofluffjobs.com/pl"
driver = webdriver.Chrome(options=chrome_driver_configuration())
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


def get_page_content(category):
    page = 1
    data = []
    while True:
        url = f"{BASE_URL}/{category}?page={page}"
        print(url)
        # try:
        driver.get(url)
        # except urllib3.exceptions.MaxRetryError as e:
        #     print(f"Error: {e}")
        #     time.sleep(10)  # Wait and then retry
        #     continue

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        jobs = soup.find("div", class_="list-container ng-star-inserted")

        a_tag = soup.find("a")
        if not a_tag:
            break
        if not jobs:
            break
        page += 1

        if jobs:
            data.append(jobs)
        time.sleep(2)

    # driver.quit()
    return data


def extract_job_offers(jobs):
    if jobs:
        job_list = jobs.find_all("a")
        for job in job_list:
            data = {}

            job_url = job["href"]
            title = job.find(
                "h3",
                class_="posting-title__position text-truncate color-main ng-star-inserted",
            )
            company = job.find(
                "span",
                class_="d-block posting-title__company text-truncate",
            )
            salary = job.find(
                "span",
                class_="text-truncate badgy salary tw-btn tw-btn-secondary-outline tw-btn-xs ng-star-inserted",
            )
            localization = job.find(
                "span",
                class_="tw-text-ellipsis tw-inline-block tw-overflow-hidden tw-whitespace-nowrap lg:tw-max-w-[100px] tw-text-right",
            )
            if title and company and salary and localization and job_url:
                data["url"] = f"{BASE_URL}{job_url}"
                data["title"] = title.text
                data["company"] = company.text
                data["salary"] = salary.text
                data["localization"] = localization.text
                print(data)


for category in categories:
    jobs = get_page_content(category)
    for job in jobs:
        extract_job_offers(job)
