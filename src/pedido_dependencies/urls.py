from rest_framework import routers

from pedido_dependencies.api.viewsets import (
    PedidoDependenciesViewset, ItemPedidoDependenciesViewset
)

pedido_router = routers.DefaultRouter()
pedido_router.register('pedidos', PedidoDependenciesViewset, basename='pedido-api')
pedido_router.register('itens_pedido', ItemPedidoDependenciesViewset, basename='itens-pedido-api')
