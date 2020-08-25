from django.db import models

class Vendedor(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    cpf = models.CharField(max_length=11, verbose_name='CPF')

    class Meta:
        db_table = 'vendedor'

    def __str__(self):
        return self.nome
