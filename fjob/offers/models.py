from django.db import models


class Salary(models.Model):
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    contract_type = models.CharField(max_length=20, null=True, blank=True)
    work_schedule = models.CharField(max_length=20, null=True, blank=True)


class Offers(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    offer_id = models.CharField(max_length=255, null=True, blank=True)
    salary = models.ManyToManyField(Salary)
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
