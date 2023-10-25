from typing import Optional
from dataclasses import dataclass


@dataclass
class ParamsData:
    """
    Dataclass for storing params data
    """

    type: Optional[str] = None
    agreement: Optional[bool] = None
    salary_from: Optional[int] = None
    salary_to: Optional[int] = None
    currency: Optional[str] = None
    experience: Optional[bool] = None
    availability: Optional[str] = None
    workplace: Optional[str] = None
    salary_schedule: Optional[str] = None
