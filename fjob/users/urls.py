from django.urls import path

from .views import (
    UserLogoutView,
    UserRegistrationView,
    UserPasswordChangeView,
    UserAccountDeleteView,
)

urlpatterns = [
    path("logout/", UserLogoutView.UserLogoutView.as_view(), name="logout"),
    path(
        "register/",
        UserRegistrationView.UserRegisterView.as_view(),
        name="register",
    ),
    path(
        "change-password/",
        UserPasswordChangeView.UserPasswordChangeView.as_view(),
        name="change_password",
    ),
    path(
        "account-delete/",
        UserAccountDeleteView.UserAccountDeleteView.as_view(),
        name="delete_account",
    ),
]
