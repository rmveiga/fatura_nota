from django.db import models

TIPO_NOTAFISCAL = [
    (1, 'Saída'),
    (2, 'Entrada'),
]

STATUS_NOTAFISCAL = [
    (1, 'Cadastrada'),
    (2, 'Emitida'),
    (3, 'Cancelada'),
]


class NotaFiscal(models.Model):
    tipo_notafiscal = models.IntegerField(
        choices=TIPO_NOTAFISCAL, default=1, verbose_name='Tipo de Nota Fiscal'
    )
    numero = models.IntegerField(verbose_name='Número')
    data_emissao = models.DateField(auto_now_add=True, verbose_name='Data de Emissão')
    status = models.IntegerField(
        choices=STATUS_NOTAFISCAL, editable=False, default=1, verbose_name='Status da Nota Fiscal'
    )

    class Meta:
        db_table = 'notafiscal'

    def __str__(self):
        return str(self.numero)

    # def numero_notafiscal(self):
    #     notafiscal = self.objects.all().last()
    #     if not notafiscal:
    #         return 1
    #     ultimo_numero = notafiscal.numero
    #     return ultimo_numero + 1


class ItemNotaFiscal(models.Model):
    notafiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE, verbose_name='Nota Fiscal')
    quantidade = models.FloatField(verbose_name='Quantidade')
    valor_unitario = models.FloatField(verbose_name='Valor Unitário')
    desconto_percentual = models.FloatField(null=True, blank=True, verbose_name='Desconto %')

    class Meta:
        db_table = 'item_notafiscal'
