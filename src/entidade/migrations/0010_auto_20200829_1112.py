# Generated by Django 3.1 on 2020-08-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidade', '0009_auto_20200829_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='cpf_cnpj',
            field=models.CharField(max_length=14, verbose_name='CPF/CNPJ'),
        ),
    ]