from .dynamic.olx import run as run_olx
from .dynamic.pracujpl import run as run_pracujpl
from typing import List, Dict, Any, Optional
from celery import shared_task
from .static import jjit
from .static.pracapl import PracaPL, get_max_page
from .static.theprotocol import TheProtocol
import logging


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@shared_task()
def pracujpl_task(city: str, query: str = None) -> List[Optional[Dict[str, Any]]]:
    try:
        pracujpl_data = run_pracujpl(city=city, query=query)
        print(pracujpl_data)
        return pracujpl_data
    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")
        return []


@shared_task()
def olx_task(city: str, query: str = None) -> List[Optional[Dict[str, Any]]]:
    try:
        olx_data = run_olx(city=city, query=query)
        return olx_data
    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")
        return []


def jjit_task() -> None:
    jjit_scraper = jjit.JJIT()
    jjit_scraper.fetch_data()
    x = jjit_scraper.parse_offer()
    print(x[3])


def pracapl_task() -> None:
    max_page = get_max_page()
    pracapl_scraper = PracaPL(max_page=max_page)
    pracapl_scraper.pipeline()


def theprotocol_task() -> None:
    theprotocol_scraper = TheProtocol()
    theprotocol_scraper.pipeline()
