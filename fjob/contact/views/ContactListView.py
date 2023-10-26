from ..serializers.ContactSerializer import ContactSerializer
from ..models import Contact
from fjob.pagination import CustomPagination
from fjob.permissions import IsSuerUserPermission
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ContactListView(generics.ListAPIView):
    permission_classes = [IsSuerUserPermission]
    pagination_class = CustomPagination
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["read"]
    ordering = ["-date_created"]
