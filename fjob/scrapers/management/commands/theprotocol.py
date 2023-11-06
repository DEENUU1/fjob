from django.core.management.base import BaseCommand
from ...tasks import run_the_protocol


class Command(BaseCommand):
    help = "Testing theprotocol scraper"

    def handle(self, *args, **kwargs):
        run_the_protocol()
