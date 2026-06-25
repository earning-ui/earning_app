from django.contrib import admin
from .models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'price',
        'daily_profit',
        'duration_days',
    )