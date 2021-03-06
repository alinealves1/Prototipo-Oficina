# Generated by Django 3.2.9 on 2021-11-27 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('rg', models.CharField(max_length=15, verbose_name='RG')),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('rua', models.CharField(max_length=150, verbose_name='Rua')),
                ('numero', models.CharField(max_length=10, verbose_name='Numero')),
                ('complemento', models.CharField(blank=True, max_length=120, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(default='Itapevi', max_length=50, verbose_name='Cidade')),
            ],
        ),
    ]
