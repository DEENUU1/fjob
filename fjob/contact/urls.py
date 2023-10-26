from django.urls import path

from .views import ContactCreateView, ContactMarkAsReadView, ContactListView


urlpatterns = [
    path(
        "send/",
        ContactCreateView.ContactCreateView.as_view(),
        name="send_message",
    ),
    path(
        "read/<int:pk>/",
        ContactMarkAsReadView.ContactMarkAsReadView.as_view(),
        name="mark_as_read",
    ),
    path("list/", ContactListView.ContactListView.as_view(), name="list_messages"),
]
