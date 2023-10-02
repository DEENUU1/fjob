from .models import Notification
from offers.models import Offer
from django.db.models import Q
from celery import shared_task


@shared_task()
def send_daily_notification():
    notifications = Notification.objects.all()
    queryset = Offer.objects.all()
    for notification in notifications:
        user_email = notification.user.email
        user_name = notification.user.username
        query = notification.query
        country = notification.country
        city = notification.city
        min_salary = notification.min_salary
        max_salary = notification.max_salary
        experience_level = notification.experience_level

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        if country:
            queryset = queryset.filter(country__icontains=country)
        if city:
            queryset = queryset.filter(city__icontains=city)
        if min_salary:
            queryset = queryset.filter(salary__gte=min_salary)
        if max_salary:
            queryset = queryset.filter(salary__lte=max_salary)
        if experience_level:
            queryset = queryset.filter(experience_level=experience_level)

        # TODO sent email
