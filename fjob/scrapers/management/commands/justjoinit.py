from django.core.management.base import BaseCommand
from ...tasks import run_justjoinit


class Command(BaseCommand):
    help = "Testing justjoinit scraper"

    def handle(self, *args, **kwargs):
        run_justjoinit()
