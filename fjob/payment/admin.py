from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "active", "created_at", "updated_at")
    list_filter = ("active",)
    search_fields = ("user__username", "stripe_checkout_id")


admin.site.register(Payment, PaymentAdmin)
