from django.shortcuts import get_object_or_404, redirect, render
from .models import Customer, Bank, Deposit, Withdrawal, Transfer, Collection
from .forms import CustomerForm, BankForm, DepositForm, WithdrawalForm, TransferForm, CollectionForm
from django.http import JsonResponse

def handle_form_submission(request, form_class, redirect_url, template_name, instance=None):
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=instance)
    return render(request, template_name, {'form': form})

def index(request):
    return render(request, 'customer/index.html')


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer/customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = CustomerForm()
    return render(request, 'customer/customer/customer_form.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    return handle_form_submission(request, CustomerForm, 'customer_list', 'customer/customer/customer_form.html', instance=customer)


def customer_delete(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer/customer/customer_confirm_delete.html', {'object': customer})


def bank_list(request):
    banks = Bank.objects.all()
    return render(request, 'customer/bank/bank_list.html', {'banks': banks})

def bank_create(request):
    return handle_form_submission(request, BankForm, 'bank_list', 'customer/bank/bank_form.html')

def bank_update(request, id):
    bank = get_object_or_404(Bank, id=id)
    return handle_form_submission(request, BankForm, 'bank_list', 'customer/bank/bank_form.html', instance=bank)

def bank_delete(request, id):
    bank = get_object_or_404(Bank, id=id)
    if request.method == 'POST':
        bank.delete()
        return redirect('bank_list')
    return render(request, 'customer/bank/bank_confirm_delete.html', {'object': bank})


def deposit_list(request):
    deposits = Deposit.objects.all()
    return render(request, 'customer/deposit/deposit_list.html', {'deposits': deposits})

def deposit_create(request):
    return handle_form_submission(request, DepositForm, 'deposit_list', 'customer/deposit/deposit_form.html')

def deposit_update(request, id):
    deposit = get_object_or_404(Deposit, id=id)
    return handle_form_submission(request, DepositForm, 'deposit_list', 'customer/deposit/deposit_form.html', instance=deposit)

def deposit_delete(request, id):
    deposit = get_object_or_404(Deposit, id=id)
    if request.method == 'POST':
        deposit.delete()
        return redirect('deposit_list')
    return render(request, 'customer/deposit/deposit_confirm_delete.html', {'object': deposit})


def withdrawal_list(request):
    withdrawals = Withdrawal.objects.all()
    return render(request, 'customer/withdrawal/withdrawal_list.html', {'withdrawals': withdrawals})

def withdrawal_create(request):
    return handle_form_submission(request, WithdrawalForm, 'withdrawal_list', 'customer/withdrawal/withdrawal_form.html')

def withdrawal_update(request, id):
    withdrawal = get_object_or_404(Withdrawal, id=id)
    return handle_form_submission(request, WithdrawalForm, 'withdrawal_list', 'customer/withdrawal/withdrawal_form.html', instance=withdrawal)

def withdrawal_delete(request, id):
    withdrawal = get_object_or_404(Withdrawal, id=id)
    if request.method == 'POST':
        withdrawal.delete()
        return redirect('withdrawal_list')
    return render(request, 'customer/withdrawal/withdrawal_confirm_delete.html', {'object': withdrawal})


def transfer_list(request):
    transfers = Transfer.objects.all()
    return render(request, 'customer/transfer/transfer_list.html', {'transfers': transfers})

def transfer_create(request):
    return handle_form_submission(request, TransferForm, 'transfer_list', 'customer/transfer/transfer_form.html')

def transfer_update(request, id):
    transfer = get_object_or_404(Transfer, id=id)
    return handle_form_submission(request, TransferForm, 'transfer_list', 'customer/transfer/transfer_form.html', instance=transfer)

def transfer_delete(request, id):
    transfer = get_object_or_404(Transfer, id=id)
    if request.method == 'POST':
        transfer.delete()
        return redirect('transfer_list')
    return render(request, 'customer/transfer/transfer_confirm_delete.html', {'object': transfer})


def collection_list(request):
    collections = Collection.objects.all()
    return render(request, 'customer/collection/collection_list.html', {'collections': collections})

def collection_create(request):
    return handle_form_submission(request, CollectionForm, 'collection_list', 'customer/collection/collection_form.html')

def collection_update(request, id):
    collection = get_object_or_404(Collection, id=id)
    return handle_form_submission(request, CollectionForm, 'collection_list', 'customer/collection/collection_form.html', instance=collection)

def collection_delete(request, id):
    collection = get_object_or_404(Collection, id=id)
    if request.method == 'POST':
        collection.delete()
        return redirect('collection_list')
    return render(request, 'customer/collection/collection_confirm_delete.html', {'object': collection})
