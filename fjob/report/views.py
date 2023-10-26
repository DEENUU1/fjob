from rest_framework.permissions import IsAuthenticated
from .serializers import CreateReportMessageSerializer
from .models import ReportMessage
from rest_framework import generics


class CreateReportMessage(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateReportMessageSerializer
