from django.core.management.base import BaseCommand
from offers.scrapers.olx import run


class Command(BaseCommand):
    help = "Run scraper for OLX platform"

    def handle(self, *args, **kwargs):
        run()
