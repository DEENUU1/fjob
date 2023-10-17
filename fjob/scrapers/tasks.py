from .dynamic.olx import run as run_olx
from .dynamic.pracujpl import run as run_pracujpl
from typing import List, Dict, Any
from celery import shared_task
from .static import jjit


@shared_task()
def run_scrapers() -> List[Dict[str, Any]]:
    olx_data = run_olx("Zduńska Wola")
    pracujpl_data = run_pracujpl("Zduńska Wola")
    return olx_data + pracujpl_data


def run_jjit() -> None:
    jjit_scraper = jjit.JJIT()
    jjit_scraper.fetch_data()
    x = jjit_scraper.parse_offer()
    print(x)
