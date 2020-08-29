from rest_framework import serializers

from vendedor.models import Vendedor


class VendedorSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField(source='cpf_formatado', label='CPF')

    class Meta:
        model = Vendedor
        fields = (
            'id', 'nome', 'cpf'
        )

