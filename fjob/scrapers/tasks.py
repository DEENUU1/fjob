from .scrapers.theprotocol import (
    get_content as get_content_theprotocol,
    process as process_the_protocol,
)
from .scrapers.justjoinit import (
    get_content as get_content_justjoinit,
    process as process_justjoinit,
)
from .scrapers.justjoinit.get_content import CATEGORIES
from .scrapers.pracapl import (
    get_content as get_content_pracapl,
    process as process_pracapl,
)
from .scrapers.pracujpl import (
    get_content as get_content_pracujpl,
    process as process_pracujpl,
)
from .scrapers.nfj import get_content as get_content_nfj, process as process_nfj
from .scrapers.olx import get_content as get_content_olx, process as process_olx
import logging
from .models import PageContent
from celery import shared_task


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

        page_content = PageContent.objects.filter(
            website="TheProtocol", is_parsed=False
        ).all()
        for content in page_content:
            process = process_the_protocol.TheProtocolProcess()
            process.parse_html(content.content)
            processed_data = process.process()
            for data in processed_data:
                process.save_to_db(data)

            content.delete()

    except Exception as e:
        logging.error(f"Failed to run the protocol scraper: {e}")


@shared_task
def run_justjoinit():
    try:
        for cat in CATEGORIES:
            scraper = get_content_justjoinit.GetJustJoinITContent(cat)
            scraper.fetch_content()
            logging.info(
                f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
            )
            scraper.save_to_db()

        page_content = PageContent.objects.filter(
            website="JustJoinIT", is_parsed=False
        ).all()
        for content in page_content:
            process = process_justjoinit.JJITProcess()
            process.parse_html(content.content)
            processed_data = process.process()
            process.save_to_db(processed_data)

            content.delete()

    except Exception as e:
        logging.error(f"Failed to run justjoinit  scraper: {e}")


@shared_task
def run_nfj():
    try:
        scraper = get_content_nfj.GetNFJContent()
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

        page_content = PageContent.objects.filter(website="NFJ", is_parsed=False).all()
        for content in page_content:
            process = process_nfj.NFJProcess()
            process.parse_html(content.content)
            processed_data = process.process()
            for pd in processed_data:
                process.save_to_db(pd)

            content.delete()

    except Exception as e:
        logging.error(f"Failed to run nfj scraper: {e}")


@shared_task
def run_pracapl():
    try:
        max_page = get_content_pracapl.get_max_page()
        scraper = get_content_pracapl.GetPracaPLContent(max_page)
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

        page_content = PageContent.objects.filter(
            website="PracaPL", is_parsed=False
        ).all()
        for content in page_content:
            process = process_pracapl.PracaPLProcess()
            process.parse_html(content.content)
            processed_data = process.process()
            for data in processed_data:
                process.save_to_db(data)

            content.delete()

    except Exception as e:
        logging.error(f"Failed to run pracapl scraper: {e}")


@shared_task
def run_pracujpl():
    try:
        max_page = get_content_pracujpl.get_max_page_number()
        scraper = get_content_pracujpl.GetPracujPLContent(max_page)
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

        page_content = PageContent.objects.filter(
            website="PracujPL", is_parsed=False
        ).all()
        for content in page_content:
            process = process_pracujpl.PracujPLProcess()
            process.parse_html(content.content)
            processed_data = process.process()
            for data in processed_data:
                process.save_to_db(data)

            content.delete()

    except Exception as e:
        logging.error(f"Failed to run pracujpl scraper: {e}")


@shared_task
def run_olx():
    try:
        scraper = get_content_olx.GetOLXContent()
        scraper.fetch_content()
        logging.info(
            f"Successfully fetched content for {scraper.website} get {scraper.__len__()} elements"
        )
        scraper.save_to_db()

        page_content = PageContent.objects.filter(website="OLX", is_parsed=False).all()

        for content in page_content:
            process = process_olx.OLXProcess()
            process.parse_html(content.content_json)
            processed_data = process.process()
            for data in processed_data:
                process.save_to_db(data)

            content.delete()

    except Exception as e:
        logging.error(f"Failed to run olx scraper: {e}")
