from django.urls import path

from .views import (
    GetPackages,
    GetUserFreeUses,
    CreateCheckoutSession,
    SuccessView,
    CancelView,
    GetUserPackage,
)

urlpatterns = [
    path("", GetPackages.GetPackages.as_view(), name="get_packages"),
    path(
        "user-free-uses",
        GetUserFreeUses.GetUserFreeUses.as_view(),
        name="user_free_uses",
    ),
    path(
        "chs/<int:package_id>/",
        CreateCheckoutSession.CreateCheckoutSession.as_view(),
        name="chs",
    ),
    path("success/<str:custom_id>/", SuccessView.SuccessView.as_view(), name="success"),
    path("cancel", CancelView.CancelView.as_view(), name="cancel"),
    path("user-package", GetUserPackage.GetUserPackage.as_view(), name="user_package"),
]
