from django.shortcuts import render, redirect
from .forms import DepositForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import DepositForm


@login_required
def deposit(request):

    if request.method == 'POST':

        form = DepositForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()

            return redirect('dashboard')

    else:
        form = DepositForm()

    return render(
        request,
        'payments/deposit.html',
        {'form': form}
    )

from .forms import DepositForm, WithdrawalForm
from .models import Withdrawal


@login_required
def withdraw(request):

    if request.method == 'POST':

        form = WithdrawalForm(request.POST)

        if form.is_valid():

            withdrawal = form.save(commit=False)
            withdrawal.user = request.user

            # Prevent withdrawal if balance is too low
            if request.user.wallet_balance < withdrawal.amount:

                return render(
                    request,
                    'payments/withdraw.html',
                    {
                        'form': form,
                        'error': 'Insufficient wallet balance.'
                    }
                )

            withdrawal.save()

            return redirect('dashboard')

    else:
        form = WithdrawalForm()

    return render(
        request,
        'payments/withdraw.html',
        {
            'form': form
        }
    )