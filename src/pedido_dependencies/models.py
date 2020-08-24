from django.db import models

from pedido.models import Pedido, ItemPedido
from entidade.models import Entidade
from vendedor.models import Vendedor
from estoque.models import Produto


class PedidoDependencies(Pedido):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, verbose_name='Entidade')
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, verbose_name='Vendedor')

    class Meta:
        db_table = 'pedido_dependencies'


class ItemPedidoDependencies(ItemPedido):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')

    class Meta:
        db_table = 'item_pedido_dependencies'
