from django.core.management.base import BaseCommand
from ...tasks import jjit_task


class Command(BaseCommand):
    help = "Run JJIT scraper"

    def handle(self, *args, **kwargs):
        jjit_task()
