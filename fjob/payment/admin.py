from django.contrib import admin
from .models import Package, Payment, UserPackage


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "has_signals",
        "num_of_signals",
        "is_free",
        "free_users",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_free",)
    search_fields = ("name",)


class PaymentAdmin(admin.ModelAdmin):
    # list_display = ("user", "package", "stripe_checkout_id", "created_at", "updated_at")
    # list_filter = ("user", "package")
    # search_fields = ("user__username",)
    pass


class UserPackageAdmin(admin.ModelAdmin):
    list_display = ("user", "package", "active", "created_at", "updated_at")
    list_filter = ("user", "package", "active")
    search_fields = ("user__username",)


admin.site.register(Package, PackageAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserPackage, UserPackageAdmin)
