from .scrapers.olx.olx import OLX
from celery import shared_task
import logging

logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


@shared_task()
def olx_task() -> None:
    try:
        olx_scraper = OLX()
        olx_scraper.run()
    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")
        return
