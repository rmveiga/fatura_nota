from django.db import models

from utilitario import validadores

validador = validadores.Validador()

TIPO_MOVIMENTO_ESTOQUE = [
    (1, 'Saída'),
    (2, 'Entrada'),
]


class Produto(models.Model):
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    _preco_venda = models.FloatField(
        null=True, blank=True, verbose_name='Preço de Venda', name='preco_venda'
    )
    bloqueado = models.BooleanField(default=False, verbose_name='Bloqueado')
    observacao = models.TextField(null=True, blank=True, verbose_name='Observação')

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.descricao

    @property
    def preco_venda(self):
        return self._preco_venda

    @preco_venda.setter
    def preco_venda(self, value):
        validador.valida_preco_venda_produto_api(value)
        self._preco_venda = value

class MovimentoEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
    data_movimento = models.DateField(auto_now_add=True, verbose_name='Data do Movimento')
    tipo_movimento = models.IntegerField(choices=TIPO_MOVIMENTO_ESTOQUE, verbose_name='Tipo de Movimento')
    _quantidade = models.FloatField(verbose_name='Quantidade', name='quantidade')
    _preco_venda = models.FloatField(
        null=True, blank=True, verbose_name='Preço de Venda', name='preco_venda'
    )
    observacao = models.TextField(null=True, blank=True, verbose_name='Observação')

    class Meta:
        db_table = 'movimento_estoque'

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, value):
        validador.valida_quantidade_produto_api(value)
        self._quantidade = value

    @property
    def preco_venda(self):
        return self._preco_venda

    @preco_venda.setter
    def preco_venda(self, value):
        validador.valida_preco_venda_produto_api(value)
        self._preco_venda = value

