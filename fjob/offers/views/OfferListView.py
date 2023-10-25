from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from ..models import Offers
from ..serializers.OfferSerializer import OffersSerializer
from ..forms import OffersFilter
from django_filters import rest_framework as filters


class OfferListView(generics.ListAPIView):
    authentication_classes = [
        IsAuthenticated,
    ]
    queryset = Offers.objects.filter(is_active=True)
    serializer_class = OffersSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_class = OffersFilter
    ordering_fields = [
        "-date_scraped",
        "date_scraped",
        "salary__salary_from",
        "-salary__salary_from",
    ]
