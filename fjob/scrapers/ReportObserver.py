from dashboard.models import Report


class ReportObserver:
    def __init__(self, scraper_name):
        self.scraper_name = scraper_name

    def create_report(self, number_of_scraped_data):
        report = Report.objects.create(
            scraper_name=self.scraper_name,
            number_of_scraped_data=number_of_scraped_data,
        )
        report.save()
