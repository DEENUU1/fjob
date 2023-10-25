from django.urls import path

from .views import OfferFilterView

urlpatterns = [
    path("", OfferFilterView.OffersListView.as_view(), name="offers"),
]
