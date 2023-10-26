from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from ..serializers.ExperienceLevelSerializer import ExperienceLevelSerializer
from ..models import ExperienceLevel


class ExperienceLevelListView(ListAPIView):
    serializer_class = ExperienceLevelSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ExperienceLevel.objects.all()
