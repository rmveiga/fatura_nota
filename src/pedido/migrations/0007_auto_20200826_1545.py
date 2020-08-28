# Generated by Django 3.1 on 2020-08-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0006_pedido_tipo_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='tipo_pedido',
            field=models.IntegerField(choices=[(1, 'Saída'), (2, 'Entrada')], default=1, verbose_name='Tipo de Pedido'),
        ),
    ]