from django import forms
from .models import Deposit, Withdrawal


from django import forms
from .models import Deposit


from django import forms
from .models import Deposit, Withdrawal


class DepositForm(forms.ModelForm):

    class Meta:
        model = Deposit
        fields = [
            'amount',
            'payment_method',
            'transaction_id',
            'screenshot'
        ]


class WithdrawalForm(forms.ModelForm):

    class Meta:
        model = Withdrawal
        fields = [
            'amount',
            'method',
            'account_number'
        ]