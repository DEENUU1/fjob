from django.core.management.base import BaseCommand
from ...tasks import theprotocol_task


class Command(BaseCommand):
    help = "Run TheProtocol scraper"

    def handle(self, *args, **kwargs):
        theprotocol_task()
