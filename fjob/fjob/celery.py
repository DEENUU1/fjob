from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fjob.settings")
app = Celery("fjob")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     "check-medicine-expiration-every-day": {
#         "task": "medicine.tasks.send_medicine_expired_notification",
#         "schedule": 86400,  # Every 24H
#     },
#     "send-dish-every-day": {
#         "task": "social.tasks.send_random_dish_to_newsletter_users",
#         "schedule": 86400,  # Every 24H
#     },
# }
