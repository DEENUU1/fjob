from django.urls import path
from . import views


urlpatterns = [
    path(
        "register",
        views.UserRegistrationView.UserRegisterView.as_view(),
        name="register",
    ),
    path("login", views.UserLoginView.UserLoginView.as_view(), name="login"),
    path("logout", views.UserLogoutView.UserLogoutView.as_view(), name="logout"),
]
