from .scrapers.theprotocol import get_content as get_content_theprotocol
from .scrapers.justjoinit import get_content as get_content_justjoinit
from .scrapers.pracapl import get_content as get_content_pracapl
from .scrapers.pracujpl import get_content as get_content_pracujpl
from .scrapers.nfj import get_content as get_content_nfj
import logging


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def run_the_protocol():
    try:
        scraper = get_content_theprotocol.GetTheProtocolContent()
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

    except Exception as e:
        logging.error(f"Failed to run the protocol scraper: {e}")


def run_justjoinit():
    try:
        scraper = get_content_justjoinit.GetJustJoinITContent()
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

    except Exception as e:
        logging.error(f"Failed to run justjoinit  scraper: {e}")


def run_pracapl():
    try:
        max_page = get_content_pracapl.get_max_page()
        scraper = get_content_pracapl.GetPracaPLContent(max_page)
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

    except Exception as e:
        logging.error(f"Failed to run pracapl scraper: {e}")


def run_pracujpl():
    try:
        max_page = get_content_pracujpl.get_max_page_number()
        scraper = get_content_pracujpl.GetPracujPLContent(max_page)
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

    except Exception as e:
        logging.error(f"Failed to run pracujpl scraper: {e}")


def run_nfj():
    try:
        scraper = get_content_nfj.GetNFJContent()
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

    except Exception as e:
        logging.error(f"Failed to run nfj scraper: {e}")
