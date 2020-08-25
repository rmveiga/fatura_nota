# Generated by Django 3.1 on 2020-08-25 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendedor', '0001_initial'),
        ('estoque', '0001_initial'),
        ('entidade', '0003_endereco_tipoendereco'),
        ('pedido', '0005_auto_20200825_0856'),
        ('notafiscal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotaFiscalDependencies',
            fields=[
                ('notafiscal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notafiscal.notafiscal')),
                ('entidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidade.entidade', verbose_name='Entidade')),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido', verbose_name='Pedido')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendedor.vendedor', verbose_name='Vendedor')),
            ],
            options={
                'db_table': 'notafiscal_dependencies',
            },
            bases=('notafiscal.notafiscal',),
        ),
        migrations.CreateModel(
            name='ItemNotaFiscalDependencies',
            fields=[
                ('itemnotafiscal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notafiscal.itemnotafiscal')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto', verbose_name='Produto')),
            ],
            options={
                'db_table': 'item_notafiscal_dependencies',
            },
            bases=('notafiscal.itemnotafiscal',),
        ),
    ]
