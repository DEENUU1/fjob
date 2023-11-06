from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from fjob.pagination import CustomPagination
from ..models import Offers
from ..serializers.OfferSerializer import OffersSerializer
from ..forms import OffersFilter
from django_filters import rest_framework as filters
from django.views.decorators.cache import cache_page


class OfferListView(generics.ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Offers.objects.filter(is_active=True)
    serializer_class = OffersSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = OffersFilter
    pagination_class = CustomPagination
    ordering_fields = [
        "-date_scraped",
        "date_scraped",
        "salary__salary_from",
        "-salary__salary_from",
    ]
    search_fields = ["title", "description", "skills"]

    # @method_decorator(cache_page(60))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
