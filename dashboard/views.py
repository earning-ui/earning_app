from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import User
from payments.models import Deposit, Withdrawal
from investments.models import Investment


@login_required
def dashboard(request):

    deposits = Deposit.objects.filter(user=request.user)
    withdrawals = Withdrawal.objects.filter(user=request.user)
    investments = Investment.objects.filter(user=request.user)

    context = {
        'deposits': deposits,
        'withdrawals': withdrawals,
        'investments': investments,
    }

    return render(request, 'dashboard/dashboard.html', context)