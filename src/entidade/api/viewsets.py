from rest_framework import viewsets

from entidade.api.serializers import (
    EntidadeSerializer, TelefoneSerializer, EnderecoSerializer
)
from entidade.models import (
    Entidade, Telefone, Endereco
)


class EntidadeViewset(viewsets.ModelViewSet):
    queryset = Entidade.objects.all()
    serializer_class = EntidadeSerializer


class TelefoneViewset(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer


class EnderecoViewset(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
