from django.core.management.base import BaseCommand
from ...scraper_main import run_the_justjoinit


class Command(BaseCommand):
    help = "Testing justjoinit scraper"

    def handle(self, *args, **kwargs):
        run_the_justjoinit()
