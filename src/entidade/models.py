from django.db import models

class Entidade(models.Model):
    data_cadastro = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=14)
    observacao = models.TextField(null=True, blank=True)
    cliente = models.BooleanField()
    fornecedor = models.BooleanField()

    class Meta:
        db_table = 'entidade'

    def __str__(self):
        return self.nome
    