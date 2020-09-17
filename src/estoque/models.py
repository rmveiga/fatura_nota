from django.db import models
from django.utils import timezone

from utilitario import validadores

validador = validadores.Validador()

TIPO_MOVIMENTO_ESTOQUE = [
    (1, 'Saída'),
    (2, 'Entrada'),
]


class Produto(models.Model):
    descricao = models.CharField(max_length=150, verbose_name='Descrição')
    preco_venda = models.FloatField(
        blank=True, validators=[validador.valida_preco_venda_produto], verbose_name='Preço de Venda'
    )
    bloqueado = models.BooleanField(default=False, editable=False, verbose_name='Bloqueado')
    observacao = models.TextField(blank=True, default='', verbose_name='Observação')

    objects = models.Manager

    class Meta:
        db_table = 'produto'

    def __str__(self):
        return self.descricao


class MovimentoEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
    data_registro = models.DateField(auto_now_add=True, verbose_name='Data do Registro do Movimento')
    data_movimento = models.DateField(default=timezone.now, verbose_name='Data do Movimento')
    tipo_movimento = models.IntegerField(choices=TIPO_MOVIMENTO_ESTOQUE, verbose_name='Tipo de Movimento')
    quantidade = models.FloatField(verbose_name='Quantidade')
    valor = models.FloatField(blank=True, default=0, verbose_name='Valor')
    observacao = models.TextField(blank=True, default='', verbose_name='Observação')

    objects = models.Manager

    class Meta:
        db_table = 'movimento_estoque'
