from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ('Personal info', {"fields": ("first_name", "last_name", "email")}),
        (
            'Permissions',
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ('Important dates', {"fields": ("last_login", "date_joined")}),
        ('Addition data', {"fields": ('phone', 'is_verified_phone')}),
    )
