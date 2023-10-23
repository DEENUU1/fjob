from django.urls import path

from .views import (
    UserLogoutView,
    UserLoginView,
    UserRegistrationView,
    UserPasswordChangeView,
    UserAccountDeleteView,
    CheckAuthenticatedView,
    GetCSRToken,
)

urlpatterns = [
    path("logout/", UserLogoutView.UserLogoutView.as_view(), name="logout"),
    path(
        "register",
        UserRegistrationView.UserRegisterView.as_view(),
        name="register",
    ),
    path("login", UserLoginView.UserLoginView.as_view(), name="login"),
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
    path(
        "authenticated",
        CheckAuthenticatedView.CheckAuthenticatedView.as_view(),
        name="authenticated",
    ),
    path("csrf_cookie", GetCSRToken.GetCSRFToken.as_view(), name="csrf_cookie"),
]
