from bs4 import BeautifulSoup
import httpx


BASE_URL = f"https://www.praca.pl/oferty-pracy_"


def get_max_page() -> int:
    response = httpx.get(f"{BASE_URL}1")
    soup = BeautifulSoup(response.text, "html.parser")
    pagination = soup.find("a", class_="pagination__item--last")
    if pagination:
        return int(pagination.text)
    else:
        return 1


def fetch_data(page_num: int):
    response = httpx.get(f"{BASE_URL}{page_num}")
    return response.text


max_page = get_max_page()
for i in range(1, max_page + 1):
    fetch_data(i)
    print(f"Fetched page {i}")
