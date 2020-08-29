# Generated by Django 3.1 on 2020-08-29 00:42

from django.db import migrations, models
import django.db.models.deletion
import entidade.util


class Migration(migrations.Migration):

    dependencies = [
        ('entidade', '0006_auto_20200828_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='cpf_cnpj',
            field=models.CharField(max_length=14, validators=[entidade.util.Validador.valida_cpf_cnpj_api], verbose_name='CPF/CNPJ'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='tipo_telefone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entidade.tipotelefone', verbose_name='Tipo de Telefone'),
        ),
    ]
