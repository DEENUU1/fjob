from .models import Contact
from celery import shared_task
from datetime import datetime, timedelta


@shared_task
def delete_old_contacts() -> None:
    ninty_days_ago = datetime.now() - timedelta(days=90)
    contacts_to_delete = Contact.objects.filter(date_created__lt=ninty_days_ago)
    contacts_to_delete.delete()
