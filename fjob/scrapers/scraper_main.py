from .scrapers.theprotocol import get_content
from .scrapers.justjoinit import get_content
import logging


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def run_the_protocol():
    try:
        scraper = get_content.GetTheProtocolContent()
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

    except Exception as e:
        logging.error(f"Failed to run the protocol scraper: {e}")


def run_the_justjoinit():
    try:
        scraper = get_content.GetJustJoinITContent()
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

    except Exception as e:
        logging.error(f"Failed to run justjoinit  scraper: {e}")
