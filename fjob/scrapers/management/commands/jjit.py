from django.core.management.base import BaseCommand
from ...tasks import run_jjit


class Command(BaseCommand):
    help = "Run JJIT scraper"

    def handle(self, *args, **kwargs):
        run_jjit()
