# Generated by Django 3.1 on 2020-09-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20200830_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_venda',
            field=models.FloatField(blank=True, default=0, verbose_name='Preço de Venda'),
            preserve_default=False,
        ),
    ]
