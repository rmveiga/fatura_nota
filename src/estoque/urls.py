from rest_framework import routers

from estoque.api.viewsets import (
    ProdutoViewset, MovimentoEstoqueViewset
)

estoque_router = routers.DefaultRouter()
estoque_router.register('produtos', ProdutoViewset, basename='produtos-api')
estoque_router.register('movimentos', MovimentoEstoqueViewset, basename='movimentos-estoque-api')