from django.db import models
from django.contrib.auth import get_user_model
from offers.models import Offers
from datetime import timedelta
from django.utils import timezone


User = get_user_model()


class ReportMessage(models.Model):
    message = models.CharField(max_length=255)
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.offer} | {self.message[:50]}"

    class Meta:
        ordering = ("-date_created",)
        verbose_name = "Report Message"
        verbose_name_plural = "Report Messages"

    @property
    def is_new(self):
        time_diff = timezone.now() - self.date_created
        return time_diff < timedelta(days=1)
