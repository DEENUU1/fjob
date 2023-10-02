from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'country', 'city', 'min_salary', 'max_salary', 'experience_level')
    list_filter = ('country', 'experience_level')
    search_fields = ('user__username', 'query', 'city')


admin.site.register(Notification, NotificationAdmin)
