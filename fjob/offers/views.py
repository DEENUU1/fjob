from rest_framework.generics import ListAPIView
from .models import Offers
from .serializers import OffersSerializer
from .forms import OfferFilterForm
from rest_framework.exceptions import ValidationError
from django.db.models import Q


class OfferFilterView(ListAPIView):
    serializer_class = OffersSerializer
    filter_form_class = OfferFilterForm

    def get_queryset(self):
        queryset = Offers.objects.all()

        query = self.request.query_params.get("query")
        country = self.request.query_params.get("country")
        city = self.request.query_params.get("city")
        min_salary = self.request.query_params.get("min_salary")
        max_salary = self.request.query_params.get("max_salary")
        experience_level = self.request.query_params.get("experience_level")

        if city and not country:
            raise ValidationError("City cannot be specified without a country.")
        if country and not city:
            raise ValidationError("Country cannot be specified without a city.")

        if (min_salary or max_salary) and not (query or country):
            raise ValidationError(
                "Salary range cannot be specified without a query or country."
            )

        if experience_level and not (query or country):
            raise ValidationError(
                "Experience level cannot be specified without a query or country."
            )

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

        return queryset
