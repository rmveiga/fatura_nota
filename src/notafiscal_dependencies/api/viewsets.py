from rest_framework import viewsets

from notafiscal_dependencies.api.serializers import (
    NotaFiscalDependenciesSerializer, ItemNotaFiscalDependenciesSerializer
)
from notafiscal_dependencies.models import (
    NotaFiscalDependencies, ItemNotaFiscalDependencies
)


class NotaFiscalDependenciesViewset(viewsets.ModelViewSet):
    queryset = NotaFiscalDependencies.objects.all()
    serializer_class = NotaFiscalDependenciesSerializer


class ItemNotaFiscalDependenciesViewset(viewsets.ModelViewSet):
    queryset = ItemNotaFiscalDependencies.objects.all()
    serializer_class = ItemNotaFiscalDependenciesSerializer
