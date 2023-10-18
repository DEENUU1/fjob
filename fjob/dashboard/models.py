from django.db import models


class Report(models.Model):
    scraper_name = models.CharField(max_length=50)
    number_of_scraped_data = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.scraper_name} - {self.number_of_scraped_data} - {self.date}"

    class Meta:
        verbose_name_plural = "Reports"
        ordering = ["-date"]
        verbose_name = "Report"
