from rest_framework import viewsets, status
from rest_framework.response import Response

from pedido_dependencies.api.serializers import (
    PedidoDependenciesSerializer, ItemPedidoDependenciesSerializer
)
from pedido_dependencies.models import (
    PedidoDependencies, ItemPedidoDependencies
)

from utilitario import documentos


class PedidoDependenciesViewset(viewsets.ModelViewSet):
    queryset = PedidoDependencies.objects.all()
    serializer_class = PedidoDependenciesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ultimo_pedido = PedidoDependencies.objects.all().last()
        numero_pedido = documentos.gera_numero_pedido(ultimo_pedido)
        serializer.validated_data.update({'numero': numero_pedido})

        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ItemPedidoDependenciesViewset(viewsets.ModelViewSet):
    queryset = ItemPedidoDependencies.objects.all()
    serializer_class = ItemPedidoDependenciesSerializer
