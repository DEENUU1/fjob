from django.core.management.base import BaseCommand
from ...tasks import run_pracapl


class Command(BaseCommand):
    help = "Testing pracapl scraper"

    def handle(self, *args, **kwargs):
        run_pracapl()
