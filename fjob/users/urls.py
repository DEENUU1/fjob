from django.urls import path

from .views import (
    UserLogoutView,
    UserLoginView,
    UserRegistrationView,
    UserPasswordChangeView,
    UserAccountDeleteView,
)

urlpatterns = [
    path(
        "register",
        UserRegistrationView.UserRegisterView.as_view(),
        name="register",
    ),
    path("login", UserLoginView.UserLoginView.as_view(), name="login"),
    path("logout", UserLogoutView.UserLogoutView.as_view(), name="logout"),
    path(
        "change-password",
        UserPasswordChangeView.UserPasswordChangeView.as_view(),
        name="change_password",
    ),
    path(
        "account-delete",
        UserAccountDeleteView.UserAccountDeleteView.as_view(),
        name="delete_account",
    ),
]
