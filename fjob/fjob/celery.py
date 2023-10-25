from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fjob.settings")
app = Celery("fjob")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "daily-olx-scraping": {
        "task": "scrapers.tasks.olx_task",
        "schedule": 86400,  # Every 24H
    },
}
