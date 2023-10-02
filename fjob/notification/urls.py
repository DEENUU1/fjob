from django.urls import path

from .views import (
    NotificationCreateView,
    NotificationDeleteView,
    NotificationUpdateView,
)


urlpatterns = [
    path("create/", NotificationCreateView.as_view(), name="notification_create"),
    path(
        "<int:pk>/update/", NotificationUpdateView.as_view(), name="notification_update"
    ),
    path(
        "<int:pk>/delete/", NotificationDeleteView.as_view(), name="notification_delete"
    ),
]
