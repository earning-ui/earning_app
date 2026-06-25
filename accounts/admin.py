from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):

    model = User

    list_display = (
        'id',
        'username',
        'email',
        'wallet_balance',
        'referred_by',
        'is_staff',
        'is_active',
    )

    list_filter = (
        'is_staff',
        'is_active',
    )


admin.site.register(User, CustomUserAdmin)