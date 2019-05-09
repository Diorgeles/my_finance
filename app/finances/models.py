from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class ExpenseAndReceive(SoftDeletableModel, TimeStampedModel):
    """Model definition for ExpenseAndReceive."""

    EXPENSE_RECEIVE_TYPE = [
        ('expense', 'Depesa'),
        ('receive', 'Receita'),
    ]

    description = models.CharField('Descrição', max_length=100)
    price = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    paid = models.BooleanField('Pago', default=True)
    expense_receive_type = models.CharField(
        'Tipo', max_length=50, choices=EXPENSE_RECEIVE_TYPE)

    class Meta:
        """Meta definition for ExpenseAndReceive."""

        verbose_name = 'Despesa e Receita'
        verbose_name_plural = 'Despesas e Receitas'

    def __str__(self):
        """Unicode representation of ExpenseAndReceive."""
        return self.description


class Account(models.Model):
    """Model definition for Account."""

    ACCOUNT_TYPE = [
        ('wallet', 'Carteira'),
        ('checking_account', 'Conta Corrente'),
    ]

    description = models.CharField('Descrição', max_length=100)
    initial_balance = models.DecimalField(
        'Balanço inicial', max_digits=8, decimal_places=2)
    account_type = models.CharField(
        'Tipo de Conta', max_length=50, choices=ACCOUNT_TYPE)

    class Meta:
        """Meta definition for Account."""

        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    def __str__(self):
        """Unicode representation of Account."""
        return self.description


class Category(models.Model):
    """Model definition for Category."""

    CATEGORY_TYPE = [
        ('expense', 'Despesa'),
        ('receive', 'Receita'),
        ('account', 'Conta'),
    ]

    description = models.CharField('Descrição', max_length=100)
    category_type = models.CharField(
        'Tipo de Categoria', max_length=50, choices=CATEGORY_TYPE)
    icon = models.ImageField(
        'Icone', upload_to=None, height_field=None, width_field=None)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        """Unicode representation of Category."""
        return self.description
