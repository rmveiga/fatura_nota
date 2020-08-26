from django.db import models

TIPO_PEDIDO = [
    (1, 'Saída'),
    (2, 'Entrada'),
]

STATUS_PEDIDO = [
    (1, 'Cadastrado'),
    (2, 'Faturado'),
    (3, 'Cancelado'),
]


class Pedido(models.Model):
    tipo_pedido = models.IntegerField(
        choices=TIPO_PEDIDO, default=1, verbose_name='Tipo de Pedido'
    )
    numero = models.IntegerField(verbose_name='Número')
    data_emissao = models.DateField(auto_now_add=True, verbose_name='Data de Emissão')
    status = models.IntegerField(
        choices=STATUS_PEDIDO, default=1, editable=False, verbose_name='Status do Pedido'
    )

    class Meta:
        db_table = 'pedido'

    def __str__(self):
        return str(self.numero)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
    quantidade = models.FloatField(verbose_name='Quantidade')
    valor_unitario = models.FloatField(verbose_name='Valor Unitário')
    desconto_percentual = models.FloatField(null=True, blank=True, verbose_name='Desconto %')

    class Meta:
        db_table = 'item_pedido'
