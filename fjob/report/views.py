from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ReportMessage
from .serializers import (
    ReportMessageSerializer,
    UpdateReportMessageSerializer,
    CreateReportMessageSerializer,
)
from fjob.permissions import IsSuerUserPermission
from rest_framework.permissions import IsAuthenticated
from fjob.pagination import CustomPagination


class ReportMessageCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ReportMessage.objects.all()
    serializer_class = CreateReportMessageSerializer


class ReportMessageUpdateView(generics.UpdateAPIView):
    permission_classes = [IsSuerUserPermission, IsAuthenticated]
    queryset = ReportMessage.objects.all()
    serializer_class = UpdateReportMessageSerializer

    def perform_update(self, serializer):
        serializer.save(reviewed=True)
        serializer.save()
        return super().perform_update(serializer)


class ReportMessageListView(generics.ListAPIView):
    permission_classes = [IsSuerUserPermission, IsAuthenticated]
    pagination_class = CustomPagination
    queryset = ReportMessage.objects.all()
    serializer_class = ReportMessageSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["reviewed"]
    ordering = ["-date_created"]
