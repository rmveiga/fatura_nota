from rest_framework import serializers

from estoque.models import Produto, MovimentoEstoque


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = (
            'id', 'descricao', 'preco_venda', 'bloqueado', 'observacao'
        )


class MovimentoEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentoEstoque
        fields = (
            'id', 'produto', 'data_movimento', 'tipo_movimento', 'quantidade',
            'preco_venda', 'observacao'
        )
