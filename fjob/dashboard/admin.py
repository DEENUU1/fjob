from django.contrib import admin
from .models import Report, UserStats


class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "scraper_name", "user", "number_of_scraped_data", "date")
    list_filter = ("scraper_name", "date", "user")
    search_fields = ("scraper_name", "date", "user")
    ordering = ("-date",)


class UserStatsAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "number_of_usage")
    ordering = ("-number_of_usage",)


admin.site.register(Report, ReportAdmin)
admin.site.register(UserStats, UserStatsAdmin)
