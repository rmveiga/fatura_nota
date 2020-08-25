from rest_framework import viewsets

from estoque.api.serializers import (
    ProdutoSerializer, MovimentoEstoqueSerializer
)
from estoque.models import Produto, MovimentoEstoque


class ProdutoViewset(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class MovimentoEstoqueViewset(viewsets.ModelViewSet):
    queryset = MovimentoEstoque.objects.all()
    serializer_class = MovimentoEstoqueSerializer
