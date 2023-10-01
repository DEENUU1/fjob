from datetime import timedelta

from django.db import models
from django.utils import timezone

from ..models.salaries import Salaries


class Offers(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    offer_id = models.CharField(max_length=255, null=True, blank=True)
    salary = models.ManyToManyField(Salaries)
    url = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    additional_data = models.JSONField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    remote = models.BooleanField(null=True, blank=True)
    hybrid = models.BooleanField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_finished = models.DateTimeField(null=True, blank=True)
    experience_level = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_logo = models.CharField(max_length=255, null=True, blank=True)
    date_scraped = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:
        ordering = ("-date_scraped",)
        verbose_name = "Offer"
        verbose_name_plural = "Offers"

    def __str__(self):
        return self.title

    @property
    def is_new(self):
        time_diff = timezone.now() - self.date_scraped
        return time_diff < timedelta(days=1)
