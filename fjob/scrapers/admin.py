from django.contrib import admin
from .models import PageContent


class PageContentAdmin(admin.ModelAdmin):
    list_display = ("website", "is_parsed", "date_created")
    list_filter = ("website", "is_parsed", "date_created")
    search_fields = ("website", "content")
    date_hierarchy = "date_created"


admin.site.register(PageContent, PageContentAdmin)
