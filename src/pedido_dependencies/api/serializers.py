from rest_framework import serializers

from pedido_dependencies.models import (
    PedidoDependencies, ItemPedidoDependencies
)


class PedidoDependenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoDependencies
        fields = (
            'id', 'entidade', 'vendedor', 'tipo_pedido', 'numero', 'data_emissao', 'status'
        )


class ItemPedidoDependenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedidoDependencies
        fields = (
            'id', 'pedido', 'produto', 'quantidade', 'valor_unitario', 'desconto_percentual'
        )
