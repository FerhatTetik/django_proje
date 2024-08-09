from django.contrib import admin
from .models import Deposit, Withdrawal, Transfer, Collection

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('date', 'account_number', 'get_customer_name', 'amount', 'description', 'status')
    list_filter = ('status', 'date')
    search_fields = ('account_number', 'customer__first_name', 'customer__last_name')
    date_hierarchy = 'date'

    def get_customer_name(self, obj):
        return obj.customer.full_name
    get_customer_name.short_description = 'Customer Name'

@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('date', 'account_number', 'get_customer_name', 'amount', 'description', 'status')
    list_filter = ('status', 'date')
    search_fields = ('account_number', 'customer__first_name', 'customer__last_name')
    date_hierarchy = 'date'

    def get_customer_name(self, obj):
        return obj.customer.full_name
    get_customer_name.short_description = 'Customer Name'

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('date', 'sender_account', 'receiver_account', 'amount', 'description', 'status')
    list_filter = ('status', 'date')
    search_fields = ('sender_account__first_name', 'sender_account__last_name', 
                     'receiver_account__first_name', 'receiver_account__last_name')
    date_hierarchy = 'date'

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('date', 'get_customer_name', 'invoice_number', 'amount_collected', 'description', 'status')
    list_filter = ('status', 'date')
    search_fields = ('invoice_number', 'customer__first_name', 'customer__last_name')
    date_hierarchy = 'date'

    def get_customer_name(self, obj):
        return obj.customer.full_name
    get_customer_name.short_description = 'Customer Name'
