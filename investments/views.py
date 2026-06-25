from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from packages.models import Package
from .models import Investment


@login_required
def buy_package(request, package_id):

    package = get_object_or_404(
        Package,
        id=package_id
    )

    user = request.user

    # Check wallet balance
    if user.wallet_balance < package.price:
        return redirect('dashboard')

    # Deduct package price from wallet
    user.wallet_balance -= package.price
    user.save()

    # Create investment
    Investment.objects.create(
        user=user,
        package=package,
        amount=package.price
    )

    # Referral commission (5%)
    if user.referred_by:

        sponsor = user.referred_by

        commission = package.price * 0.05

        sponsor.wallet_balance += commission
        sponsor.referral_earnings += commission

        sponsor.save()

    return redirect('dashboard')