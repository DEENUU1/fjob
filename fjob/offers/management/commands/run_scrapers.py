from django.core.management.base import BaseCommand
from scrapers.tasks import run_scrapers


class Command(BaseCommand):
    help = "Run scraper for OLX platform"

    def handle(self, *args, **kwargs):
        data = run_scrapers()
        print(data)
