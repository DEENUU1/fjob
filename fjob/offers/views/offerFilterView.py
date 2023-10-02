from django.db.models import Q
from rest_framework.generics import ListAPIView

from ..forms import OfferFilterForm
from ..models import offers
from ..serializers import OffersSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from scrapers.tasks import run_scrapers


class OfferFilterView(ListAPIView):
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
            advanced_data = run_scrapers.delay()
            queryset = list(queryset) + list(advanced_data)

        return queryset

    @method_decorator(cache_page(60 * 1))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
