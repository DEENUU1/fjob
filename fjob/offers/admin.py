from django.contrib import admin
from .models import Salary, Offers


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "salary_from",
        "salary_to",
        "currency",
        "contract_type",
        "work_schedule",
    )
    list_filter = ("currency", "contract_type", "work_schedule")
    search_fields = ("currency", "contract_type", "work_schedule")


@admin.register(Offers)
class OffersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "offer_id",
        "url",
        "street",
        "region",
        "remote",
        "hybrid",
        "date_created",
        "date_finished",
    )
    list_filter = (
        "remote",
        "hybrid",
        "experience_level",
        "date_created",
        "date_finished",
    )
    search_fields = (
        "title",
        "offer_id",
        "region",
        "experience_level",
        "skills",
        "company_name",
    )
