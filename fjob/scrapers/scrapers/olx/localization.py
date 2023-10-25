from typing import Optional
from dataclasses import dataclass


@dataclass
class Localization:
    """
    Dataclass for storing localization data
    """

    region: Optional[str] = None
    city: Optional[str] = None
