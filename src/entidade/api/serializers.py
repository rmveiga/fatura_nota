from rest_framework import serializers

from entidade.models import Entidade, Telefone, Endereco


class EntidadeSerializer(serializers.ModelSerializer):
    cpf_cnpj = serializers.CharField(source='cpf_cnpj_formatado', label='CPF/CNPJ')

    class Meta:
        model = Entidade
        fields = (
            'id', 'data_cadastro', 'nome', 'cpf_cnpj', 'observacao', 'cliente', 'fornecedor'
        )


class TelefoneSerializer(serializers.ModelSerializer):
    numero = serializers.CharField(source='numero_formatado')

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
