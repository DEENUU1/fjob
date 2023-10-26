from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from ..serializers.WorkScheduleSerializer import WorkScheduleSerializer
from ..models import WorkSchedule


class WorkScheduleListView(ListAPIView):
    serializer_class = WorkScheduleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return WorkSchedule.objects.all()
