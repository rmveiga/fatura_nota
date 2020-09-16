# Generated by Django 3.1 on 2020-09-16 19:46

from django.db import migrations, models
import utilitario.validadores


class Migration(migrations.Migration):

    dependencies = [
        ('entidade', '0015_auto_20200916_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidade',
            name='cpf_cnpj',
            field=models.CharField(max_length=14, validators=[utilitario.validadores.Validador.valida_cpf_cnpj], verbose_name='CPF/CNPJ'),
        ),
    ]
