from django.contrib import admin
from .models import ReferralCommission


@admin.register(ReferralCommission)
class ReferralCommissionAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'referred_user',
        'amount',
        'created_at',
    )