from rest_framework import serializers

from vendedor.models import Vendedor


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = (
            'id', 'nome', 'cpf'
        )

