from django.urls import path

from .views import (
    OfferListView,
    OfferCountView,
    OfferDetailsView,
    OfferDeleteView,
    OfferUpdateView,
)

urlpatterns = [
    path("", OfferListView.OfferListView.as_view(), name="offers"),
    path(
        "<int:pk>/", OfferDetailsView.OfferDetailsView.as_view(), name="offer_details"
    ),
    path(
        "delete/<int:pk>/",
        OfferDeleteView.OfferDeleteView.as_view(),
        name="offer_delete",
    ),
    path(
        "update/<int:pk>/",
        OfferUpdateView.OfferUpdateView.as_view(),
        name="offer_update",
    ),
    path("number/", OfferCountView.OfferCountView.as_view(), name="offer_count"),
]
