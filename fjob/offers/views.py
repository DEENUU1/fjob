from rest_framework.generics import ListAPIView
from .models import Offers, Salaries
from .serializers import OffersSerializer, SalariesSerializer
from .forms import OfferFilterForm


class OfferFilterView(ListAPIView):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer
    filter_form_class = OfferFilterForm

    def get_queryset(self):
        queryset = self.queryset

        query = self.request.query_params.get("query")
        country = self.request.query_params.get("country")
        city = self.request.query_params.get("city")
        min_salary = self.request.query_params.get("min_salary")
        max_salary = self.request.query_params.get("max_salary")
        experience_level = self.request.query_params.get("experience_level")

        if query:
            queryset = queryset.filter(title__icontains=query)
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

        return queryset
