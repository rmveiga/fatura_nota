from rest_framework import serializers

from entidade.models import Entidade

class EntidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidade
        fields = (
            'id', 'data_cadastro', 'nome', 'cpf_cnpj', 'observacao', 'cliente', 'fornecedor'
        )