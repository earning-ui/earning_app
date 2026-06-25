from django.contrib import admin
from .models import Deposit, Withdrawal


# =========================
# APPROVE DEPOSITS
# =========================
@admin.action(description="Approve selected deposits")
def approve_deposits(modeladmin, request, queryset):

    for deposit in queryset:

        if deposit.status == "Pending":
            deposit.status = "Approved"
            deposit.save()

            user = deposit.user
            user.wallet_balance += deposit.amount
            user.save()


# =========================
# DEPOSIT ADMIN
# =========================
@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'amount',
        'payment_method',
        'status',
        'created_at'
    )

    actions = [approve_deposits]


# =========================
# APPROVE WITHDRAWALS
# =========================
@admin.action(description="Approve selected withdrawals")
def approve_withdrawals(modeladmin, request, queryset):

    for w in queryset:

        if w.status == "Pending":
            user = w.user

            # check balance safety
            if user.wallet_balance >= w.amount:

                user.wallet_balance -= w.amount
                user.save()

                w.status = "Approved"
                w.save()

            else:
                w.status = "Rejected"
                w.save()


# =========================
# WITHDRAWAL ADMIN
# =========================
@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'amount',
        'method',
        'status',
        'created_at'
    )

    actions = [approve_withdrawals]