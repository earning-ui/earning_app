from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):

    wallet_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    referral_code = models.CharField(
        max_length=12,
        unique=True,
        blank=True,
        null=True
    )

    referred_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='referrals'
    )

    # IMPORTANT: add this to fix old migration error
    referral_earnings = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)