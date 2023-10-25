from datetime import timedelta
from django.db import models
from django.utils import timezone


class Website(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ("-name",)
        verbose_name = "Website"
        verbose_name_plural = "Websites"

    def __str__(self):
        return self.name


class ExperienceLevel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("-name",)
        verbose_name = "Experience Level"
        verbose_name_plural = "Experience Levels"

    def __str__(self):
        return self.name


class Salaries(models.Model):
    SALARY_SCHEDULE = [
        (1, "Monthly"),
        (2, "Yearly"),
        (3, "Hourly"),
    ]
    TYPE = [
        (1, "Brutto"),
        (2, "Netto"),
    ]
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    contract_type = models.CharField(max_length=20, null=True, blank=True)
    work_schedule = models.CharField(max_length=20, null=True, blank=True)
    salary_schedule = models.IntegerField(
        choices=SALARY_SCHEDULE, null=True, blank=True
    )
    type = models.IntegerField(choices=TYPE, null=True, blank=True)

    class Meta:
        ordering = ("-salary_from",)
        verbose_name = "Salary"
        verbose_name_plural = "Salaries"

    def __str__(self):
        return f"{self.salary_from} - {self.salary_to}"


class Localization(models.Model):
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ("-country",)
        verbose_name = "Localization"
        verbose_name_plural = "Localizations"

    def __str__(self):
        return f"{self.country}, {self.city}, {self.region}, {self.street}"


class Offers(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_logo = models.CharField(max_length=255, null=True, blank=True)
    is_remote = models.BooleanField(default=False)
    is_hybrid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_promoted = models.BooleanField(default=False)
    date_created = models.DateTimeField(null=True, blank=True)
    date_finished = models.DateTimeField(null=True, blank=True)
    date_scraped = models.DateTimeField(auto_now=True)
    experience_level = models.ManyToManyField(ExperienceLevel, blank=True)
    salary = models.ManyToManyField(Salaries, blank=True)
    website = models.ForeignKey(
        Website, on_delete=models.CASCADE, null=True, blank=True
    )
    localizations = models.ManyToManyField(Localization, blank=True)

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
