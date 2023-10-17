import httpx
from bs4 import BeautifulSoup


response = httpx.get("https://theprotocol.it/")
soup = BeautifulSoup(response.text, "html.parser")
job_cards = soup.find_all("a", class_="anchorClass_a6of9et")

for card in job_cards:
    title = card.find("h2", class_="titleText_t1280ha4")
    company_logo = card.find("img")
    details = card.find_all("div", class_="rootClass_rpqnjlt")
    skill_divs = card.find_all("div", {"data-test": "chip-expectedTechnology"})
    skills = []
    if skill_divs:
        for div in skill_divs:
            spans = div.find_all("span", class_="Label_l1fs6hs4")
            for span in spans:
                skills.append(span.text)
    localization = card.find("div", {"data-test": "text-workplaces"})
    d = {}
    for idx, detail in enumerate(details):
        if idx == 0:
            d["company_name"] = detail

        if idx == 1:
            d["work_mode"] = detail

    if title:
        print(title.text)
    if company_logo:
        print(company_logo["src"])
    if d.get("company_name", None):
        print(d["company_name"].text)
    if d.get("company_logo", None):
        print(d["company_logo"].text)
    if skills:
        print(skills)
    if localization:
        print(localization.text)

    print("\n\n\n")
