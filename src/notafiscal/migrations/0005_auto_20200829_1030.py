# Generated by Django 3.1 on 2020-08-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notafiscal', '0004_auto_20200826_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemnotafiscal',
            name='desconto_percentual',
            field=models.FloatField(blank=True, default=0, verbose_name='Desconto %'),
        ),
    ]
