# Generated by Django 3.1 on 2020-08-30 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='movimentoestoque',
            table='movimento_estoque',
        ),
    ]