from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from users.views.CustomTokenObtainPairView import CustomTokenObtainPairView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/offers/", include("offers.urls")),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/messages/", include("contact.urls")),
    path("api/v1/reports/", include("report.urls")),
    path(
        "api/v1/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/v1/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
