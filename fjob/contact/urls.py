from django.urls import path

from . import views

urlpatterns = [
    path(
        "send",
        views.SendMessage.as_view(),
        name="send_message",
    ),

]
