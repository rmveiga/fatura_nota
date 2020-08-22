from django.db import models


TIPO_MOVIMENTO_ESTOQUE = [
    (1, 'Saída'),
    (2, 'Entrada'),
]


class Produto(models.Model):
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    preco_venda = models.FloatField(null=True, blank=True, verbose_name='Preço de Venda')
    bloqueado = models.BooleanField(default=False, verbose_name='Bloqueado')
    observacao = models.TextField(null=True, blank=True, verbose_name='Observação')

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.descricao

class MovimentoEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
    data_movimento = models.DateField(auto_now_add=True, verbose_name='Data do Movimento')
    tipo_movimento = models.IntegerField(choices=TIPO_MOVIMENTO_ESTOQUE, verbose_name='Tipo de Movimento')
    quantidade = models.FloatField(verbose_name='Quantidade')
    preco_venda = models.FloatField(null=True, blank=True, verbose_name='Preço de Venda')
    observacao = models.TextField(null=True, blank=True, verbose_name='Observação')


