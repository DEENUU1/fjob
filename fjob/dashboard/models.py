from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Report(models.Model):
    scraper_name = models.CharField(max_length=50)
    number_of_scraped_data = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.scraper_name} - {self.number_of_scraped_data} - {self.date}"

    class Meta:
        verbose_name_plural = "Reports"
        ordering = ["-date"]
        verbose_name = "Report"


class UserStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_usage = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.number_of_usage}"

    class Meta:
        verbose_name_plural = "User Stats"
        ordering = ["-number_of_usage"]
        verbose_name = "User Stats"
