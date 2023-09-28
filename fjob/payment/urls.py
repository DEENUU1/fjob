from django.urls import path
from . import views

urlpatterns = [
    path("chs", views.CreateCheckoutSession.as_view(), name="chs"),
    path("success", views.SuccessView.as_view(), name="success"),
    path("cancel", views.CancelView.as_view(), name="cancel"),
]
