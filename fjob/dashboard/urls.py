from django.urls import path

from .views import ReportListVIew

urlpatterns = [
    path("", ReportListVIew.ReportListView.as_view(), name="report_list"),
]
