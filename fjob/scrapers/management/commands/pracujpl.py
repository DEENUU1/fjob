from django.core.management.base import BaseCommand
from ...scraper_main import run_pracujpl


class Command(BaseCommand):
    help = "Testing pracujpl scraper"

    def handle(self, *args, **kwargs):
        run_pracujpl()
