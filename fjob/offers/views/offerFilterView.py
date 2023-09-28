from rest_framework import status
from rest_framework.generics import ListAPIView
from ..models import offers
from ..serializers import OffersSerializer
from ..forms import OfferFilterForm
from django.db.models import Q
from scrapers import olx, pracujpl
from payment.models import Payment
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response


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

        # if the user does not use advanced search, he will only receive offers from the database
        if not advanced:
            return queryset

        # however, when using advanced search, it will receive offers from the database and scrapers will be launched
        else:
            payment = Payment.objects.filter(
                user=self.request.user, active=True
            ).first()
            if not payment:
                return Response(
                    {"error": "YOu need an active payment to use advanced search"},
                    status=status.HTTP_403_FORBIDDEN,
                )
            else:
                olx_data = olx.run(False, False, "Zduńska Wola")
                pracujpl_data = pracujpl.run(False, False, "Zduńska Wola")
                advanced_queryset = list(queryset) + olx_data + pracujpl_data

                return advanced_queryset
