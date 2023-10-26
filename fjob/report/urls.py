from django.urls import path
from .views import CreateReportMessage


urlpatterns = [
    path("create/", CreateReportMessage.as_view(), name="create_report_message"),
]
