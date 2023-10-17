from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "https://justjoin.it/all-locations/ux"
PIXELS_TO_SCROLL = "500"
driver = webdriver.Chrome()
driver.get(BASE_URL)
data = []


def extract_job_offers():
    try:
        elements = driver.find_elements(By.CLASS_NAME, "css-gfqoze")
        for element in elements:
            data.append(element)
    except Exception as e:
        print(e)


def scroll():
    try:
        while True:
            last_height = driver.execute_script("return window.scrollY")
            extract_job_offers()
            driver.execute_script(
                f"window.scrollTo(0, window.scrollY + {PIXELS_TO_SCROLL});"
            )
            time.sleep(1)

            new_height = driver.execute_script("return window.scrollY")
            if new_height == last_height:
                break
    except Exception as e:
        print(e)


scroll()
print(len(data))
