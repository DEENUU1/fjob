from django.core.management.base import BaseCommand
from ...tasks import olx_task


class Command(BaseCommand):
    help = "Run OLX scraper"

    def add_arguments(self, parser):
        parser.add_argument("city", type=str, help="City name")
        parser.add_argument("--query", type=str, help="Query")

    def handle(self, *args, **kwargs):
        city = kwargs["city"]
        query = kwargs["query"]

        print(olx_task(city, query))
        # TODO add delay here
