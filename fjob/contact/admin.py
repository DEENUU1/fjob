from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "read", "date_created")
    list_filter = ("date_created", "read")
    search_fields = ("name", "email")
    ordering = ("-date_created",)
