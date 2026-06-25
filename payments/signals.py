from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Withdrawal

@receiver(post_save, sender=Withdrawal)
def deduct_wallet_on_approval(sender, instance, created, **kwargs):

    if instance.status == "Approved":
        user = instance.user

        # Safety check (no negative balance)
        if user.wallet_balance >= instance.amount:
            user.wallet_balance -= instance.amount
            user.save()