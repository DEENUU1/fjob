from django.db import models


class Salaries(models.Model):
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    contract_type = models.CharField(max_length=20, null=True, blank=True)
    work_schedule = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ("-salary_from",)
        verbose_name = "Salary"
        verbose_name_plural = "Salaries"

    def __str__(self):
        return f"{self.salary_from} - {self.salary_to}"
