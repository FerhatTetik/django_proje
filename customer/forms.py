from django import forms
from .models import Customer, Bank,Deposit, Withdrawal, Transfer, Collection



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = '__all__'

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'
