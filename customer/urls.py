from django.urls import path
from . import views
from .views import (
    customer_list, customer_create, customer_update, customer_delete,
    bank_list, bank_create, bank_update, bank_delete,
    deposit_list, deposit_create, deposit_update, deposit_delete,
    withdrawal_list, withdrawal_create, withdrawal_update, withdrawal_delete,
    transfer_list, transfer_create, transfer_update, transfer_delete,
    collection_list, collection_create, collection_update, collection_delete,
)

urlpatterns = [
    path('', views.index, name='index'),

    path('customers/', customer_list, name='customer_list'),
    path('customers/create/', customer_create, name='customer_create'),
    path('customers/<int:pk>/update/', customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', customer_delete, name='customer_delete'),

    path('banks/', bank_list, name='bank_list'),
    path('banks/create/', bank_create, name='bank_create'),
    path('banks/<int:pk>/update/', bank_update, name='bank_update'),
    path('banks/<int:pk>/delete/', bank_delete, name='bank_delete'),

    path('deposits/', deposit_list, name='deposit_list'),
    path('deposits/create/', deposit_create, name='deposit_create'),
    path('deposits/<int:pk>/update/', deposit_update, name='deposit_update'),
    path('deposits/<int:pk>/delete/', deposit_delete, name='deposit_delete'),

    path('withdrawals/', withdrawal_list, name='withdrawal_list'),
    path('withdrawals/create/', withdrawal_create, name='withdrawal_create'),
    path('withdrawals/<int:pk>/update/', withdrawal_update, name='withdrawal_update'),
    path('withdrawals/<int:pk>/delete/', withdrawal_delete, name='withdrawal_delete'),

    path('transfers/', transfer_list, name='transfer_list'),
    path('transfers/create/', transfer_create, name='transfer_create'),
    path('transfers/<int:pk>/update/', transfer_update, name='transfer_update'),
    path('transfers/<int:pk>/delete/', transfer_delete, name='transfer_delete'),

    path('collections/', collection_list, name='collection_list'),
    path('collections/create/', collection_create, name='collection_create'),
    path('collections/<int:pk>/update/', collection_update, name='collection_update'),
    path('collections/<int:pk>/delete/', collection_delete, name='collection_delete'),
]
