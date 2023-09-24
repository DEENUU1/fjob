from requests_html import HTMLSession

url = "https://nofluffjobs.com/pl/backend?page=1"

session = HTMLSession()
r = session.get(url)
r.html.render()

# Wybierz wszystkie oferty wewnątrz diva o klasie 'list-container ng-star-inserted'
offers = r.html.find("div.list-container.ng-star-inserted a")

for offer in offers:
    # Wydobądź URL
    url = offer.attrs["href"]

    title_selector = offer.find("h3.posting-title__position", first=True)
    title_text = title_selector.text.strip() if title_selector else "None"

    # Wydobądź widełki (salary ranges)
    salary_selector = offer.find("span.text-truncate.badgy.salary", first=True)
    salary_text = salary_selector.text.strip() if salary_selector else "None"

    # Wydobądź lokalizację
    location_selector = offer.find("span.tw-text-ellipsis", first=True)
    location_text = location_selector.text.strip() if location_selector else "None"

    # Wyświetl dane oferty
    print("URL:", url)
    print("Tytuł:", title_text)
    print("Widełki:", salary_text)
    print("Lokalizacja:", location_text)
    print()
