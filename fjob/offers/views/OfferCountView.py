from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Offers
from ..serializers.OfferCounterSerializer import OfferCounterSerializer


class OfferCountView(APIView):
    def get(self, request):
        count = Offers.objects.filter(is_active=True).count()
        serializer = OfferCounterSerializer({"count": count})

        return Response(serializer.data)
