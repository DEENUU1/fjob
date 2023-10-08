from django.urls import path

from .views import SendMessage


urlpatterns = [
    path(
        "send",
        SendMessage.SendMessage.as_view(),
        name="send_message",
    ),
]
