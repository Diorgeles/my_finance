from django.contrib import admin
from .models import ExpenseAndReceive, Category, Account


@admin.register(ExpenseAndReceive)
class ExpenseAndReceiveAdmin(admin.ModelAdmin):
    '''Admin View for ExpenseAndReceive'''

    list_display = ['description', 'price', 'paid', 'expense_receive_type']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ['description', 'initial_balance', 'account_type']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Account'''

    list_display = ['description', 'category_type', 'icon']
