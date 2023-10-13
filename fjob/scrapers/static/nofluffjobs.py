from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def chrome_driver_configuration() -> Options:
    """
    Configures Chrome WebDriver options for Selenium.

    This static method creates a set of options that can be passed to the Chrome WebDriver
    when creating an instance of it. These options modify the behavior of the Chrome browser
    during automated testing or scraping.

    Returns:
        Options: A configured ChromeOptions instance to be used with Chrome WebDriver.
    """
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    chrome_options.add_argument(
        "--enable-features=NetworkService,NetworkServiceInProcess"
    )
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return chrome_options


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

driver = webdriver.Chrome(options=chrome_driver_configuration())
BASE_URL = "https://nofluffjobs.com/pl/"

for category in categories:
    page = 1
    while True:
        url = f"{BASE_URL}{category}?page={page}"
        print(url)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        jobs = soup.find("div", class_="list-container ng-star-inserted")

        a_tag = soup.find("a")
        if not a_tag:
            break

        if jobs:
            job_list = jobs.find_all("a")
            for job in job_list:
                data = {}

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
                if title and company and salary and localization:
                    data["title"] = title.text
                    data["company"] = company.text
                    data["salary"] = salary.text
                    data["localization"] = localization.text
                    print(data)
        else:
            break
        page += 1

driver.quit()
