from rest_framework import serializers

from notafiscal_dependencies.models import (
    NotaFiscalDependencies, ItemNotaFiscalDependencies
)


class NotaFiscalDependenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscalDependencies
        fields = (
            'id', 'pedido', 'entidade', 'vendedor', 'tipo_notafiscal', 'numero', 'data_emissao',
            'status'
        )


class ItemNotaFiscalDependenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemNotaFiscalDependencies
        fields = (
            'id', 'notafiscal', 'produto', 'quantidade', 'valor_unitario', 'desconto_percentual'
        )
