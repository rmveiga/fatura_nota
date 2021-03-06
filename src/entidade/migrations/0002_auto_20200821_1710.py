# Generated by Django 3.1 on 2020-08-21 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTelefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'db_table': 'tipo_telefone',
            },
        ),
        migrations.AlterField(
            model_name='entidade',
            name='cliente',
            field=models.BooleanField(verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='cpf_cnpj',
            field=models.CharField(max_length=14, verbose_name='CPF/CNPJ'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, verbose_name='Data de Cadastro'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='fornecedor',
            field=models.BooleanField(verbose_name='Fornecedor'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='nome',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='observacao',
            field=models.TextField(blank=True, null=True, verbose_name='Observação'),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_pais', models.CharField(max_length=3, verbose_name='Código do País')),
                ('ddd', models.CharField(max_length=2, verbose_name='DDD')),
                ('numero', models.CharField(max_length=9, verbose_name='Número')),
                ('ramal', models.CharField(max_length=5, verbose_name='Ramal')),
                ('entidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidade.entidade', verbose_name='Entidade')),
                ('tipo_telefone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidade.tipotelefone', verbose_name='Tipo de Telefone')),
            ],
            options={
                'db_table': 'telefone',
            },
        ),
    ]
