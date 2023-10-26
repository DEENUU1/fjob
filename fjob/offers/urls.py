from django.urls import path

from .views import OfferListView, OfferCountView

urlpatterns = [
    path("", OfferListView.OfferListView.as_view(), name="offers"),
    path("number/", OfferCountView.OfferCountView.as_view(), name="offer_count"),
]
