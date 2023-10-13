from selenium import webdriver
from bs4 import BeautifulSoup
import time
from chrome_driver import chrome_driver_configuration


BASE_URL = "https://bulldogjob.pl/companies/jobs/s/page,"
driver = webdriver.Chrome(options=chrome_driver_configuration())


def get_page_content():
    page = 1
    data = []
    while True:
        url = f"{BASE_URL}{page}"
        print(url)
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        jobs = soup.find("div", class_="container")

        if not jobs:
            break
        page += 1

        if jobs:
            data.append(jobs)

        time.sleep(10)

    return data


def extract_job_offers(jobs):
    if jobs:
        job_list = jobs.find_all("a")
        print(job_list)
        for job in job_list:
            data = {}

            job_url = job["href"]
            title = job.find(
                "h3",
                class_="md:mb-5 lg:mb-0 text-18 font-extrabold leading-8 mr-8 md:mr-0",
            )

            if title:
                # data["url"] = f"{BASE_URL}{job_url}"
                # data["title"] = title.text

                print(title.text)


jobs = get_page_content()
for job in jobs:
    extract_job_offers(job)
