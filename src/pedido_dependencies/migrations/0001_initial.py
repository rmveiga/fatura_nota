# Generated by Django 3.1 on 2020-08-24 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendedor', '0001_initial'),
        ('pedido', '0001_initial'),
        ('entidade', '0003_endereco_tipoendereco'),
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoDependencies',
            fields=[
                ('pedido_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pedido.pedido')),
                ('entidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidade.entidade', verbose_name='Entidade')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedor.vendedor', verbose_name='Vendedor')),
            ],
            options={
                'db_table': 'pedido_dependencies',
            },
            bases=('pedido.pedido',),
        ),
        migrations.CreateModel(
            name='ItemPedidoDependencies',
            fields=[
                ('itempedido_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pedido.itempedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto', verbose_name='Produto')),
            ],
            options={
                'db_table': 'item_pedido_dependencies',
            },
            bases=('pedido.itempedido',),
        ),
    ]
