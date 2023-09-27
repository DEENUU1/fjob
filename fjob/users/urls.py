from django.urls import path
from .views import UserLogoutView, UserLoginView, UserRegistrationView

urlpatterns = [
    path(
        "register",
        UserRegistrationView.UserRegisterView.as_view(),
        name="register",
    ),
    path("login", UserLoginView.UserLoginView.as_view(), name="login"),
    path("logout", UserLogoutView.UserLogoutView.as_view(), name="logout"),
]
