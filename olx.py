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
