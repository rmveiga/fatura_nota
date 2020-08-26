# Generated by Django 3.1 on 2020-08-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notafiscal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notafiscal',
            name='tipo_notafiscal',
            field=models.IntegerField(choices=[(1, 'Saída'), (2, 'Entrada')], default=1, verbose_name='Tipo de Nota Fiscal'),
            preserve_default=False,
        ),
    ]
