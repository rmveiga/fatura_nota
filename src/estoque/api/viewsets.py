from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from estoque.api.serializers import (
    ProdutoSerializer, MovimentoEstoqueSerializer
)
from estoque.models import Produto, MovimentoEstoque


class ProdutoViewset(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def update(self, request, *args, **kwargs):
        id_produto = kwargs.get('pk')
        produto = Produto.objects.get(pk=id_produto)
        if produto.bloqueado:
            raise ValidationError('Não é permitido editar um produto bloqueado')

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class MovimentoEstoqueViewset(viewsets.ModelViewSet):
    queryset = MovimentoEstoque.objects.all()
    serializer_class = MovimentoEstoqueSerializer
