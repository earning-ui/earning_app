from django.contrib import admin
from .models import Investment


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'package',
        'amount',
        'active',
    )

    list_filter = (
        'active',
    )

    search_fields = (
        'user__username',
    )