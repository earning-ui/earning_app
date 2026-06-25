from django.db import models
from django.conf import settings
from packages.models import Package


class Investment(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    start_date = models.DateTimeField(
        auto_now_add=True
    )

    active = models.BooleanField(
        default=True
    )

    days_completed = models.IntegerField(
        default=0
    )

    total_profit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"{self.user.username} - {self.package.name}"