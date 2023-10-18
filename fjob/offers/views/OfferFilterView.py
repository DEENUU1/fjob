from django.db.models import Q
from rest_framework.views import APIView
from offers.forms import OfferFilterForm
from offers.models import offers
from offers.serializers.OfferSerializer import OffersSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from offers.strategy.strategy import strategy
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from payment.models import UserPackage, Package
from payment.utils import update_free_uses
from rest_framework.permissions import IsAuthenticated


class OfferFilterView(APIView):
    authentication_classes = [
        SessionAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = OffersSerializer
    filter_form_class = OfferFilterForm

    # @method_decorator(cache_page(60 * 1))
    def get(self, request):
        query = self.request.query_params.get("query")
        country = self.request.query_params.get("country")
        if country is None:
            return Response({"message": "Country is required"})
        city = self.request.query_params.get("city")
        if city is None:
            return Response({"message": "City is required"})
        min_salary = self.request.query_params.get("min_salary")
        max_salary = self.request.query_params.get("max_salary")
        experience_level = self.request.query_params.get("experience_level")
        advanced = self.request.query_params.get("advanced")
        user = request.user

        queryset = offers.Offers.objects.all()

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
            user_package = UserPackage.objects.filter(user=user, active=True).first()
            if user_package.package.id in [2, 3]:
                advanced_data = strategy(country, city, query)
                if advanced_data:
                    queryset = list(queryset) + advanced_data
                else:
                    pass

            if user_package.package.id == 1:
                if user_package.free_uses > 0:
                    advanced_data = strategy(country, city, query)
                    if advanced_data:
                        queryset = list(queryset) + advanced_data
                    if advanced_data and len(advanced_data) != 0:
                        update_free_uses.update_free_uses(user)
                    else:
                        pass
                else:
                    return Response({"message": "You don't have any free uses"})
        return Response(OffersSerializer(queryset, many=True).data)
