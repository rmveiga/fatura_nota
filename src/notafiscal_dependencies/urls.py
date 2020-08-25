from rest_framework import routers

from notafiscal_dependencies.api.viewsets import (
    NotaFiscalDependenciesViewset, ItemNotaFiscalDependenciesViewset
)

notafiscal_router = routers.DefaultRouter()
notafiscal_router.register(
    'notasfiscais', NotaFiscalDependenciesViewset, basename='notafiscal-api'
)
notafiscal_router.register(
    'itens_notafiscal', ItemNotaFiscalDependenciesViewset, basename='itens-notafiscal-api'
)
