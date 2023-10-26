from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from ..serializers.ContractTypeSerializer import ContractTypeSerializer
from ..models import ContractType


class ContractTypeListView(ListAPIView):
    serializer_class = ContractTypeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ContractType.objects.all()
