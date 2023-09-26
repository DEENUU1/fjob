from django.core.management.base import BaseCommand
from scrapers.pracujpl import run


class Command(BaseCommand):
    help = "Run scraper for Pracuj.pl platform"

    def handle(self, *args, **kwargs):
        run(
            sfd=False,  # Do not save fetch data to json file,
            spd=False,  # Do not save parsed data to json file
            city="Zduńska Wola",
        )
