from rest_framework import viewsets

from pedido_dependencies.api.serializers import (
    PedidoDependenciesSerializer, ItemPedidoDependenciesSerializer
)
from pedido_dependencies.models import (
    PedidoDependencies, ItemPedidoDependencies
)


class PedidoDependenciesViewset(viewsets.ModelViewSet):
    queryset = PedidoDependencies.objects.all()
    serializer_class = PedidoDependenciesSerializer


class ItemPedidoDependenciesViewset(viewsets.ModelViewSet):
    queryset = ItemPedidoDependencies.objects.all()
    serializer_class = ItemPedidoDependenciesSerializer
