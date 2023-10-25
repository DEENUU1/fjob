from .static.olx import OLX
from .static.pracujpl import PracujPLIT
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
def pracujpl_task() -> List[Optional[Dict[str, Any]]]:
    try:
        scraper = PracujPLIT()
        scraper.run()
    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")
        return []


@shared_task()
def olx_task() -> None:
    try:
        olx_scraper = OLX()
        olx_scraper.run()

    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")
        return


def jjit_task() -> None:
    try:
        jjit_scraper = jjit.JJIT()
        jjit_scraper.fetch_data()
        parsed_offer = jjit_scraper.parse_offer()
        jjit_scraper.save_data(parsed_offer)

    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")


def pracapl_task() -> None:
    try:
        max_page = get_max_page()
        pracapl_scraper = PracaPL(max_page=max_page)
        data = pracapl_scraper.pipeline()
        pracapl_scraper.save_data(data)

    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")


def theprotocol_task() -> None:
    try:
        theprotocol_scraper = TheProtocol()
        data = theprotocol_scraper.pipeline()
        theprotocol_scraper.save_data(data)

    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")
