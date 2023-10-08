# from .models import Notification
# from offers.models import Offer
# from django.db.models import Q
# from celery import shared_task
# from django.conf import settings
# from django.core.mail import send_mail
# import requests
#
#
# @shared_task()
# def send_email_task(email, subject, message):
#     send_mail(
#         subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         [email],
#     )
#
#
# @shared_task()
# def send_daily_notification():
#     notifications = Notification.objects.all()
#     queryset = Offer.objects.all()
#     for notification_todo in notifications:
#         user_email = notification_todo.user.email
#         user_name = notification_todo.user.username
#         query = notification_todo.query
#         country = notification_todo.country
#         city = notification_todo.city
#         min_salary = notification_todo.min_salary
#         max_salary = notification_todo.max_salary
#         experience_level = notification_todo.experience_level
#
#         if query:
#             queryset = queryset.filter(
#                 Q(title__icontains=query) | Q(description__icontains=query)
#             )
#         if country:
#             queryset = queryset.filter(country__icontains=country)
#         if city:
#             queryset = queryset.filter(city__icontains=city)
#         if min_salary:
#             queryset = queryset.filter(salary__gte=min_salary)
#         if max_salary:
#             queryset = queryset.filter(salary__lte=max_salary)
#         if experience_level:
#             queryset = queryset.filter(experience_level=experience_level)
#
#         # TODO sent email
