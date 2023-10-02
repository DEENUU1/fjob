from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.authentication import SessionAuthentication
from .permissions import CanAccessNotification


class NotificationCreateView(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = [permissions.IsAuthenticated, CanAccessNotification]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


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
