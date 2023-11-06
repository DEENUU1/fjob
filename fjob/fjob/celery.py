from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fjob.settings")
app = Celery("fjob")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "scraper-olx": {
        "task": "scrapers.tasks.run_olx",
        "schedule": 86400,  # Every 24H
    },
    "scraper-pracujpl": {
        "task": "scrapers.tasks.run_pracujpl",
        "schedule": 86400,  # Every 24H
    },
    "scraper-pracapl": {
        "task": "scrapers.tasks.run_pracapl",
        "schedule": 86400,  # Every 24H
    },
    "scraper-nfj": {
        "task": "scrapers.tasks.run_nfj",
        "schedule": 86400,  # Every 24H
    },
    "scraper-justjoinit": {
        "task": "scrapers.tasks.run_justjoinit",
        "schedule": 86400,  # Every 24H
    },
    "scraper-theprotocol": {
        "task": "scrapers.tasks.run_the_protocol",
        "schedule": 86400,  # Every 24H
    },
    "delete-expired-offers": {
        "task": "offers.tasks.task_delete_offers_older_than_30_days",
        "schedule": 86400,  # Every 24H
    },
    "delete-expired-contacts": {
        "task": "contact.tasks.delete_old_contacts",
        "schedule": 86400,  # Every 24H
    },
    "delete-expired-reports": {
        "task": "report.tasks.delete_old_reports",
        "schedule": 86400,  # Every 24H
    },
}
