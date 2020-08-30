from django.db import models

from utilitario import formatadores, validadores

validador = validadores.Validador()

class Vendedor(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    cpf = models.CharField(max_length=11, verbose_name='CPF')

    class Meta:
        db_table = 'vendedor'

    def __str__(self):
        return self.nome

    @property
    def cpf_formatado(self):
        return formatadores.cpf_cnpj(self.cpf)

    @cpf_formatado.setter
    def cpf_formatado(self, value):
        validador.valida_cpf_cnpj(value)
        self.cpf = validador.remove_mascara_de_numero(value)
