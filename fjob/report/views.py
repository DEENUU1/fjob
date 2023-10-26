from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ReportMessage
from .serializers import (
    ReportMessageSerializer,
    UpdateReportMessageSerializer,
    CreateReportMessageSerializer,
)


class ReportMessageCreateView(generics.CreateAPIView):
    queryset = ReportMessage.objects.all()
    serializer_class = CreateReportMessageSerializer


class ReportMessageUpdateView(generics.UpdateAPIView):
    queryset = ReportMessage.objects.all()
    serializer_class = UpdateReportMessageSerializer

    def perform_update(self, serializer):
        serializer.save(reviewed=True)
        serializer.save()
        return super().perform_update(serializer)


class ReportMessageListView(generics.ListAPIView):
    queryset = ReportMessage.objects.all()
    serializer_class = ReportMessageSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["reviewed"]
    ordering = ["-date_created"]
