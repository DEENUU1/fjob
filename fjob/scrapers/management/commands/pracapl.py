from django.core.management.base import BaseCommand
from ...tasks import pracapl_task


class Command(BaseCommand):
    help = "Run PracaPl scraper"

    def handle(self, *args, **kwargs):
        pracapl_task()
