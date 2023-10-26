from .models import ReportMessage
from datetime import datetime, timedelta
from celery import shared_task


@shared_task()
def delete_old_reports():
    thirty_days_ago = datetime.now() - timedelta(days=30)
    reports_to_delete = ReportMessage.objects.filter(created_at__lt=thirty_days_ago)
    reports_to_delete.delete()
