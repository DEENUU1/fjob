from django.db.models import Q
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from scrapers import olx, pracujpl

from ..forms import OfferFilterForm
from ..models import offers
from ..serializers import OffersSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class OfferFilterView(ListAPIView):
    authentication_classes = [
        SessionAuthentication,
    ]
    serializer_class = OffersSerializer
    filter_form_class = OfferFilterForm

    def get_queryset(self):
        queryset = offers.Offers.objects.all()

        query = self.request.query_params.get("query")
        country = self.request.query_params.get("country")
        city = self.request.query_params.get("city")
        min_salary = self.request.query_params.get("min_salary")
        max_salary = self.request.query_params.get("max_salary")
        experience_level = self.request.query_params.get("experience_level")
        advanced = self.request.query_params.get("advanced")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        if country:
            queryset = queryset.filter(country__icontains=country)
        if city:
            queryset = queryset.filter(city__icontains=city)
        if min_salary:
            queryset = queryset.filter(salary__gte=min_salary)
        if max_salary:
            queryset = queryset.filter(salary__lte=max_salary)
        if experience_level:
            queryset = queryset.filter(experience_level=experience_level)

        if advanced:
            olx_data = olx.run(False, False, "Zduńska Wola")
            pracujpl_data = pracujpl.run(False, False, "Zduńska Wola")
            queryset = list(queryset) + olx_data + pracujpl_data

        return queryset

    @method_decorator(cache_page(60 * 1))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
