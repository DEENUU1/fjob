from rest_framework import generics
from rest_framework import permissions
from ..models import Offers
from ..serializers.OfferSerializer import OffersSerializer


class OfferDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer
    lookup_field = "pk"
