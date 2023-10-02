from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Notification(models.Model):
    COUNTRY = [
        ("Poland", "Poland"),
        ("Germany", "Germany"),
    ]
    EXPERIENCE = [
        ("Intern", "Intern"),
        ("Junior", "Junior"),
        ("Mid", "Mid"),
        ("Senior", "Senior"),
    ]
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True)
    query = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, choices=COUNTRY, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE, blank=True, null=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f"{self.user} - {self.query}"
