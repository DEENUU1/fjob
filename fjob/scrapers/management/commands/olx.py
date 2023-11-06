from django.core.management.base import BaseCommand
from ...tasks import run_olx


class Command(BaseCommand):
    help = "Run OLX scraper"

    def handle(self, *args, **kwargs):
        run_olx()
        # TODO add delay here
