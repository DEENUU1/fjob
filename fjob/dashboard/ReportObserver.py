from dashboard.models import Report, UserStats
from django.db import transaction


class ReportObserver:
    def __init__(self, scraper_name: str = None, user=None):
        self.scraper_name = scraper_name
        self.user = user

    def create_report(self, number_of_scraped_data: int) -> None:
        with transaction.atomic():
            report = Report.objects.create(
                scraper_name=self.scraper_name,
                number_of_scraped_data=number_of_scraped_data,
                user=self.user,
            )
            report.save()

    def update_user_stats(self) -> None:
        try:
            user_stats = UserStats.objects.get(user=self.user)
            user_stats.number_of_usage += 1
            user_stats.save()
        except UserStats.DoesNotExist:
            UserStats.objects.create(user=self.user, number_of_usage=1)
