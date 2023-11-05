from django.contrib import admin
from .models import Website, Offers, Salaries, Localization, ContractType, WorkSchedule


class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
    ordering = ["-name"]


class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
    ordering = ["-name"]


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]
    list_filter = ["name"]
    search_fields = ["name"]
    ordering = ["-name"]


class SalariesAdmin(admin.ModelAdmin):
    list_display = [
        "salary_from",
        "salary_to",
        "currency",
        "salary_schedule",
        "type",
    ]
    list_filter = ["currency", "salary_schedule"]
    search_fields = ["currency", "contract_type"]
    ordering = ["-salary_from"]


class LocalizationAdmin(admin.ModelAdmin):
    list_display = ["country", "city", "region", "street"]
    list_filter = ["country", "city", "region"]
    search_fields = ["country", "city", "region"]
    ordering = ["-country"]


class OffersAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "website",
        "is_active",
        "is_promoted",
        "date_scraped",
        "is_new",
    ]
    list_filter = ["is_active", "is_promoted", "date_scraped", "experience_level"]
    search_fields = ["title", "company_name", "description", "skills"]
    list_editable = ["is_active"]


admin.site.register(Offers, OffersAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Salaries, SalariesAdmin)
admin.site.register(Localization, LocalizationAdmin)
admin.site.register(ContractType, ContractTypeAdmin)
admin.site.register(WorkSchedule, WorkScheduleAdmin)
