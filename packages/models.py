from django.db import models


class Package(models.Model):

    name = models.CharField(
        max_length=100
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    daily_profit = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    duration_days = models.IntegerField(
        default=30
    )

    def __str__(self):
        return self.name