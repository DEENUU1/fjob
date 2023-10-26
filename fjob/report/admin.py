from django.contrib import admin
from .models import ReportMessage


class ReportMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "offer", "message", "reviewed", "date_created")
    list_filter = ("reviewed", "date_created")


admin.site.register(ReportMessage, ReportMessageAdmin)
