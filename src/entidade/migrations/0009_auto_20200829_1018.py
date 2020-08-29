# Generated by Django 3.1 on 2020-08-29 13:18

from django.db import migrations, models
import entidade.util


class Migration(migrations.Migration):

    dependencies = [
        ('entidade', '0008_auto_20200829_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='cpf_cnpj',
            field=models.CharField(max_length=14, validators=[entidade.util.Validador.valida_cpf_cnpj_api], verbose_name='CPF/CNPJ'),
        ),
    ]