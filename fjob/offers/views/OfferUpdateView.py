from rest_framework import generics
from ..serializers.OfferSerializer import OffersSerializer
from ..models import Offers
from fjob.permissions import IsSuerUserPermission
from rest_framework.response import Response


class OfferUpdateView(generics.UpdateAPIView):
    queryset = Offers.objects.all()
    serializer_class = OffersSerializer
    permission_classes = [IsSuerUserPermission]

    def partial_update(self, request, *args, **kwargs):
        offer = self.get_object()
        serializer = OffersSerializer(offer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
