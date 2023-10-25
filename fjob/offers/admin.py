from django.contrib import admin
from .models import Website, Offers, Salaries, Localization


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
        "contract_type",
        "work_schedule",
        "salary_schedule",
        "type",
    ]
    list_filter = ["currency", "contract_type", "work_schedule", "salary_schedule"]
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
        "company_name",
        "is_active",
        "is_promoted",
        "is_remote",
        "is_hybrid",
        "date_scraped",
    ]
    list_filter = ["is_active", "is_promoted", "is_hybrid", "is_remote"]
    search_fields = ["title", "company_name"]
    ordering = ["-date_scraped"]
    filter_horizontal = ["experience_level", "localizations", "salary"]


admin.site.register(Website, WebsiteAdmin)
admin.site.register(Salaries, SalariesAdmin)
admin.site.register(Localization, LocalizationAdmin)
admin.site.register(Offers, OffersAdmin)
