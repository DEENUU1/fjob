from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from fjob.pagination import CustomPagination
from dashboard.models import UserStats
from dashboard.serializers import UserStatsSerializer


class UserStatsListView(ListAPIView):
    pagination_class = CustomPagination
    serializer_class = UserStatsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        return UserStats.objects.all()
