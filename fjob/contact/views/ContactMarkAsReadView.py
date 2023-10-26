from rest_framework import generics
from ..models import Contact
from ..serializers.ContactUpdateSerializer import ContactUpdateSerializer
from fjob.permissions import IsSuerUserPermission


class ContactMarkAsReadView(generics.UpdateAPIView):
    permission_classes = [IsSuerUserPermission]
    queryset = Contact.objects.all()
    serializer_class = ContactUpdateSerializer

    def perform_update(self, serializer):
        serializer.save(read=True)
        serializer.save()
        return super().perform_update(serializer)
