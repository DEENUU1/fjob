from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from fjob.pagination import CustomPagination
from dashboard.models import Report
from dashboard.serializers import ReportSerializer


class ReportListView(ListAPIView):
    pagination_class = CustomPagination
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        return Report.objects.all()
