# Generated by Django 2.2.1 on 2019-05-31 02:17

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('initial_balance', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Balanço inicial')),
                ('account_type', models.CharField(choices=[('wallet', 'Carteira'), ('checking_account', 'Conta Corrente')], max_length=50, verbose_name='Tipo de Conta')),
            ],
            options={
                'verbose_name': 'Conta',
                'verbose_name_plural': 'Contas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('category_type', models.CharField(choices=[('expense', 'Despesa'), ('receive', 'Receita'), ('account', 'Conta')], max_length=50, verbose_name='Tipo de Categoria')),
                ('icon', models.ImageField(upload_to=None, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='ExpenseAndReceive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('paid', models.BooleanField(default=True, verbose_name='Pago')),
                ('expense_receive_type', models.CharField(choices=[('expense', 'Depesa'), ('receive', 'Receita')], max_length=50, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Despesa e Receita',
                'verbose_name_plural': 'Despesas e Receitas',
            },
        ),
    ]
