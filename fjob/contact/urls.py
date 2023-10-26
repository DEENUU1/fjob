from django.urls import path

from .views import SendMessage


urlpatterns = [
    path(
        "contact/",
        SendMessage.SendMessage.as_view(),
        name="send_message",
    ),
]
