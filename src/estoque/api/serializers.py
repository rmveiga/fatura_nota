from rest_framework import serializers

from datetime import datetime

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
            'id', 'produto', 'data_registro', 'data_movimento', 'tipo_movimento', 'quantidade',
            'valor', 'observacao'
        )

    def validate(self, data):
        data_atual = datetime.now().date()
        data_movimento = data.get('data_movimento')
        if data_movimento > data_atual:
            raise serializers.ValidationError('A data do movimento não pode ser posterior a data atual')
        return data