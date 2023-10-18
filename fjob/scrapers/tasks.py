from .dynamic.olx import OLXLocalization, OLX
from .dynamic.pracujpl import PracujPL
from typing import List, Dict, Any, Optional
from celery import shared_task
from .static import jjit
from .static.pracapl import PracaPL, get_max_page
from .static.theprotocol import TheProtocol
import logging
from dashboard.ReportObserver import ReportObserver


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@shared_task()
def pracujpl_task(
    city: str, query: str = None, user=None
) -> List[Optional[Dict[str, Any]]]:
    try:
        result = None
        scraper = PracujPL(
            "https://massachusetts.pracuj.pl/jobOffers/listing/multiregion"
        )

        if query:
            scraper.set_param("query", query)
        if city:
            scraper.set_param("wp", city)

        logging.info(f"Start fetching data for {scraper.url}")
        data = scraper.fetch_data()

        if data is None:
            logging.error("Failed to fetch data")
        else:
            logging.info(f"Scraped {len(data)} job offers")

            logging.info("Start parsing data")
            result = scraper.parse_offer(data)

        logging.info(f"Parsed {len(result)} job offers")

        if user:
            observer = ReportObserver("PracujPL", user)
            observer.create_report(len(result))
            observer.update_user_stats()

        return scraper.return_parsed_data(result)

    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")
        return []


@shared_task()
def olx_task(city: str, query: str = None, user=None) -> List[Optional[Dict[str, Any]]]:
    try:
        l = OLXLocalization(city)
        x = l.return_localization_data()
        olx_scraper = OLX("https://www.olx.pl/api/v1/offers/")

        if x is None:
            logging.error("Failed to scrap localization data")
        else:
            logging.info(f"Successfully scraped localization data: {x}")
            olx_scraper.set_param("city_id", str(x.city_id))
            olx_scraper.set_param("region_id", str(x.region_id))

        if query is not None:
            olx_scraper.set_param("query", query)

        logging.info(f"Scraping job offers from {olx_scraper.url}")
        data = olx_scraper.fetch_data()

        logging.info(f"Scraped {len(data)} job offers")

        result = olx_scraper.parse_offer(data)

        logging.info(f"Parsed {len(result)} job offers")

        if user:
            observer = ReportObserver("OLX", user)
            observer.create_report(len(result))
            observer.update_user_stats()

        return olx_scraper.return_parsed_data(result)

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
