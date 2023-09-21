from scraper import Scraper, ParsedOffer
from typing import Dict, List
import requests
import json


class JustJoinIT(Scraper):

    def fetch_data(self):
        r = requests.get(self.url)
        try:
            r.raise_for_status()
            return json.loads(r.content)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.JSONDecodeError as json_err:
            print(f"JSON decoding error occurred: {json_err}")
        return None

    def parse_data(self, json_data: Dict[str, str]):
        parsed_data = []
        for data in json_data:

            remote = False
            if data.get("workplace_type") == "remote":
                remote = True

            hybrid = False
            if data.get("employment_types") == "partly_remote":
                hybrid = True

            salary_info = data["employment_types"][0].get("salary")

            parsed_data.append(
                ParsedOffer(
                    title=data.get("title"),
                    salary_from=salary_info.get("from") if salary_info else None,
                    salary_to=salary_info.get("to") if salary_info else None,
                    currency=salary_info.get("currency") if salary_info else None,
                    url=f"https://www.justjoin.it/offers/{data.get('id')}",
                    street=data["multilocation"][0].get("city"),
                    remote=remote,
                    hybrid=hybrid,
                    country=data.get("country_code"),
                    city=data.get("city"),
                    date_created=data.get("published_at"),
                    experience_level=data.get("experience_level"),
                    skills=[skill["name"] for skill in data.get("skills")],
                )
            )

        return parsed_data


if __name__ == "__main__":
    c = JustJoinIT(f"https://www.justjoin.it/api/offers")

    # print("FETCHED DATA")
    # f = c.fetch_data()

    with open("data.json", "r", encoding="utf-8") as json_file:
        f = json.load(json_file)

    print("PARSED DATA")

    print(c.parse_data(f)[10])

