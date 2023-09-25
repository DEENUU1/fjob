from rest_framework.generics import ListAPIView
from .models import Offers, Salaries
from .serializers import OffersSerializer, SalariesSerializer
from .forms import OfferFilterForm


class OfferFilterView(ListAPIView):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer
    filter_form_class = OfferFilterForm
