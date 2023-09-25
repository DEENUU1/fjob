from django.urls import path
from .views import OfferFilterView


urlpatterns = [
    path("offers/", OfferFilterView.as_view(), name="offers"),
]
