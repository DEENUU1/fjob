from dashboard.models import Report
from django.db import transaction


class ReportObserver:
    def __init__(self, scraper_name: str, user=None):
        self.scraper_name = scraper_name
        self.user = user

    def create_report(self, number_of_scraped_data: int) -> Report:
        with transaction.atomic():
            report = Report.objects.create(
                scraper_name=self.scraper_name,
                number_of_scraped_data=number_of_scraped_data,
                user=self.user,
            )
            report.save()
