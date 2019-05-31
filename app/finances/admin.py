from django.contrib import admin
from .models import ExpenseAndReceive, Category, Account


@admin.register(ExpenseAndReceive)
class ExpenseAndReceiveAdmin(admin.ModelAdmin):
    '''Admin View for ExpenseAndReceive'''

    list_display = ('__all__')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('__all__')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    '''Admin View for Account'''

    list_display = ('__all__')
