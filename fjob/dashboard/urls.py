from django.urls import path

from .views import ReportListVIew, UserStatsListView

urlpatterns = [
    path("", ReportListVIew.ReportListView.as_view(), name="report_list"),
    path(
        "user_stats/", UserStatsListView.UserStatsListView.as_view(), name="user_stats"
    ),
]
