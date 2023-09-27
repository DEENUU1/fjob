from django.urls import path
from . import views


urlpatterns = [
    path("register", views.UserRegisterView.as_view(), name="register"),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]
