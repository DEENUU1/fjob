import json
from dataclasses import dataclass
import requests
from typing import Optional, List, Dict


@dataclass
class LocalizationData:
    """
    Dataclass for storing localization data
    """

    region_id: Optional[int] = None
    city_id: Optional[int] = None
    city_name: Optional[str] = None


class OLXLocalization:
    """
    Fetch localization data from OLX API
    """

    def __init__(self, city_name: str):
        self.city_name = city_name
        self.base_url = (
            f"https://www.olx.pl/api/v1/friendly-links/query-params/{self.city_name}"
        )

    def get_localization_data(self) -> dict | None:
        response = requests.get(self.base_url)
        if response.status_code != 200:
            return None
        return json.loads(response.content)

    def return_localization_data(self) -> LocalizationData | None:
        """
        Returning localization data
        """
        data = self.get_localization_data()
        if data:
            return LocalizationData(
                data["data"]["region_id"],
                data["data"]["city_id"],
                data["metadata"]["names"]["location"]["city"]["name"],
            )
        return None


if __name__ == "__main__":
    l = OLXLocalization("Zdunska-wola")
    x = l.return_localization_data()
    print(x)
