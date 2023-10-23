from django.core.management.base import BaseCommand
from ...tasks import olx_task


class Command(BaseCommand):
    help = "Run OLX scraper"

    def handle(self, *args, **kwargs):
        olx_task()
        # TODO add delay here
