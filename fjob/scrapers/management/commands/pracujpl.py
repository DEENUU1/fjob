from django.core.management.base import BaseCommand
from ...tasks import pracujpl_task


class Command(BaseCommand):
    help = "Run PracujPL scraper"

    def handle(self, *args, **kwargs):
        print(pracujpl_task())
        # TODO add delay here
