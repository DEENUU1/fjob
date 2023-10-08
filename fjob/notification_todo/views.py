from rest_framework import generics, permissions, status
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.authentication import SessionAuthentication
from .permissions import CanAccessNotification

from rest_framework.response import Response


class NotificationCreateView(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = [permissions.IsAuthenticated, CanAccessNotification]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def create(self, request, *args, **kwargs):
        user = self.request.user
        request.data["user"] = user.id
        return super().create(request, *args, **kwargs)


class NotificationUpdateView(generics.UpdateAPIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = [permissions.IsAuthenticated, CanAccessNotification]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationDeleteView(generics.DestroyAPIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = [permissions.IsAuthenticated, CanAccessNotification]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
