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
page = 1

for category in categories:
    while True:
        driver.get(f"{BASE_URL}{category}?page={page}")
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        jobs = soup.find("div", class_="list-container ng-star-inserted")
        if len(jobs) == 0:
            break
        for job in jobs:
            title = jobs.find_all(
                "h3",
                class_="posting-title__position text-truncate color-main ng-star-inserted",
            )
            for t in title:
                print(t.text)

        page += 1

driver.quit()
