from django.urls import path
from .views import (
    ReportMessageListView,
    ReportMessageCreateView,
    ReportMessageUpdateView,
)


urlpatterns = [
    path("", ReportMessageCreateView.as_view(), name="reportmessage-create"),
    path(
        "read/<int:pk>/",
        ReportMessageUpdateView.as_view(),
        name="reportmessage-update",
    ),
    path("list/", ReportMessageListView.as_view(), name="reportmessage-list"),
]
