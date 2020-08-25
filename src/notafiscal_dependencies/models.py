from django.db import models

from notafiscal.models import NotaFiscal, ItemNotaFiscal
from entidade.models import Entidade
from vendedor.models import Vendedor
from estoque.models import Produto
from pedido.models import Pedido


class NotaFiscalDependencies(NotaFiscal):
    pedido = models.ForeignKey(
        Pedido, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Pedido'
    )
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, verbose_name='Entidade')
    vendedor = models.ForeignKey(
        Vendedor, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Vendedor'
    )

    class Meta:
        db_table = 'notafiscal_dependencies'


class ItemNotaFiscalDependencies(ItemNotaFiscal):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')

    class Meta:
        db_table = 'item_notafiscal_dependencies'
