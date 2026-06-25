from django.shortcuts import render
from payments.models import Deposit, Withdrawal
from investments.models import Investment


def admin_dashboard(request):

    total_deposits = Deposit.objects.count()
    total_withdrawals = Withdrawal.objects.count()
    total_investments = Investment.objects.count()

    pending_deposits = Deposit.objects.filter(
        status='Pending'
    ).count()

    pending_withdrawals = Withdrawal.objects.filter(
        status='Pending'
    ).count()

    context = {
        'total_deposits': total_deposits,
        'total_withdrawals': total_withdrawals,
        'total_investments': total_investments,
        'pending_deposits': pending_deposits,
        'pending_withdrawals': pending_withdrawals,
    }

    return render(
        request,
        'admin_dashboard.html',
        context
    )