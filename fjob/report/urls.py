from django.urls import path
from .views import (
    ReportMessageListView,
    ReportMessageCreateView,
    ReportMessageUpdateView,
)


urlpatterns = [
    path("create/", ReportMessageCreateView.as_view(), name="reportmessage-create"),
    path(
        "reviewed/<int:pk>/",
        ReportMessageUpdateView.as_view(),
        name="reportmessage-update",
    ),
    path("", ReportMessageListView.as_view(), name="reportmessage-list"),
]
