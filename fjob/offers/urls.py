from django.urls import path

from .views import OfferListView

urlpatterns = [
    path("", OfferListView.OfferListView.as_view(), name="offers"),
]
