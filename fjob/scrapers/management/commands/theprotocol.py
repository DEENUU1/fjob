from django.core.management.base import BaseCommand
from ...tasks import run_theprotocol


class Command(BaseCommand):
    help = "Run TheProtocol scraper"

    def handle(self, *args, **kwargs):
        run_theprotocol()
