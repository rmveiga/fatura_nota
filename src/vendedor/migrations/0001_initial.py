# Generated by Django 3.1 on 2020-08-24 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
            ],
            options={
                'db_table': 'vendedor',
            },
        ),
    ]
