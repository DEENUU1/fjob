from django.urls import path

from .views import OfferListView, OfferCountView, OfferDetailsView

urlpatterns = [
    path("", OfferListView.OfferListView.as_view(), name="offers"),
    path(
        "<int:pk>/", OfferDetailsView.OfferDetailsView.as_view(), name="offer_details"
    ),
    path("number/", OfferCountView.OfferCountView.as_view(), name="offer_count"),
]
