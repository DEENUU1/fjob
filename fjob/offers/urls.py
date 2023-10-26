from django.urls import path

from .views import (
    OfferListView,
    OfferCountView,
    OfferDetailsView,
    OfferDeleteView,
    OfferUpdateView,
    WebsiteListView,
    ExperienceLevelListView,
    ContractTypeListView,
    WorkScheduleListView,
)

urlpatterns = [
    path("", OfferListView.OfferListView.as_view(), name="offers"),
    path(
        "<int:pk>/", OfferDetailsView.OfferDetailsView.as_view(), name="offer_details"
    ),
    path(
        "delete/<int:pk>/",
        OfferDeleteView.OfferDeleteView.as_view(),
        name="offer_delete",
    ),
    path(
        "update/<int:pk>/",
        OfferUpdateView.OfferUpdateView.as_view(),
        name="offer_update",
    ),
    path("websites/", WebsiteListView.WebsiteListView.as_view(), name="websites"),
    path(
        "experiences/",
        ExperienceLevelListView.ExperienceLevelListView.as_view(),
        name="experience_levels",
    ),
    path(
        "contracts/",
        ContractTypeListView.ContractTypeListView.as_view(),
        name="contracts",
    ),
    path(
        "work_schedules/",
        WorkScheduleListView.WorkScheduleListView.as_view(),
        name="work_schedules",
    ),
    path("number/", OfferCountView.OfferCountView.as_view(), name="offer_count"),
]
