from django.core.management.base import BaseCommand
from offers.scrapers.justjoitit import run


class Command(BaseCommand):
    help = "Run scraper for JustJoin.it platform"

    def handle(self, *args, **kwargs):
        run()
