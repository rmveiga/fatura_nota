from rest_framework import serializers

from entidade.models import Entidade, Telefone, Endereco
from utilitario.constantes import CODIGOS_AREA_BRASIL


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

    def validate(self, data):
        codigo_pais = data.get('codigo_pais')
        ddd_telefone = data.get('ddd')
        numero_telefone = data.get('numero')

        if codigo_pais == '55' and len(numero_telefone) < 8:
            raise serializers.ValidationError(f'ERRO: Número de telefone inválido ({numero_telefone})')
        if codigo_pais == '55' and int(ddd_telefone) not in CODIGOS_AREA_BRASIL.keys():
            raise serializers.ValidationError(f'ERRO: DDD inválido ({ddd_telefone})')
        return data


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            'id', 'entidade', 'tipo_endereco', 'cep', 'logradouro', 'numero', 'complemento',
            'cidade', 'estado', 'uf', 'pais', 'observacao'
        )
