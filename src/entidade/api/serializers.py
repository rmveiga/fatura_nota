from rest_framework import serializers

from entidade.models import Entidade, Telefone, Endereco


class EntidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidade
        fields = (
            'id', 'data_cadastro', 'nome', 'cpf_cnpj', 'observacao', 'cliente', 'fornecedor'
        )

    def validate(self, data):
        if not data['cliente'] and not data['fornecedor']:
            raise serializers.ValidationError('A entidade precisa ser um cliente, fornecedor ou ambos')
        return data

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = (
            'id', 'entidade', 'tipo_telefone', 'codigo_pais', 'ddd', 'numero', 'ramal'
        )


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            'id', 'entidade', 'tipo_endereco', 'cep', 'logradouro', 'numero', 'complemento',
            'cidade', 'estado', 'uf', 'pais', 'observacao'
        )
