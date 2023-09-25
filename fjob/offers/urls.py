from django.urls import path
from .views import offerFilterView


urlpatterns = [
    path("", offerFilterView.OfferFilterView.as_view(), name="offers"),
]
