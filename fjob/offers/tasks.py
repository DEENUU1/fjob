from celery import shared_task
from .models import Offers
from datetime import datetime, timedelta


@shared_task()
def task_delete_offers_older_than_30_days() -> None:
    thirty_days_ago = datetime.now() - timedelta(days=30)
    offers_to_delete = Offers.objects.filter(date_scraped__lt=thirty_days_ago)
    offers_to_delete.delete()
