from django.urls import path
from .views import OfferFilterView


urlpatterns = [
    path("", OfferFilterView.as_view(), name="offers"),
]
