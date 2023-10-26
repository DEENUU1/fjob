from rest_framework import generics
from ..models import Offers
from ..serializers.OfferSerializer import OffersSerializer
from fjob.permissions import IsSuerUserPermission


class OfferDeleteView(generics.DestroyAPIView):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer
    permission_classes = [IsSuerUserPermission]
