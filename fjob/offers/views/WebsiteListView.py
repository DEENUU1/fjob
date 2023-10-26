from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from ..serializers.WebsiteSerializer import WebsiteSerializer
from ..models import Website


class WebsiteListView(ListAPIView):
    serializer_class = WebsiteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Website.objects.all()
