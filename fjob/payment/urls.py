from django.urls import path
from . import views

urlpatterns = [
    path("", views.GetPackages.as_view(), name="get_packages"),
    path("user_free_uses", views.GetUserFreeUses.as_view(), name="user_free_uses"),
    path("chs/<int:package_id>/", views.CreateCheckoutSession.as_view(), name="chs"),
    path("success/<str:custom_id>/", views.SuccessView.as_view(), name="success"),
    path("cancel", views.CancelView.as_view(), name="cancel"),
]
