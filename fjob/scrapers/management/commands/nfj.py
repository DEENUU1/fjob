from django.core.management.base import BaseCommand
from ...scraper_main import run_nfj


class Command(BaseCommand):
    help = "Testing nfj scraper"

    def handle(self, *args, **kwargs):
        run_nfj()
