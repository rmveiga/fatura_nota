from rest_framework import viewsets, status
from rest_framework.response import Response

from notafiscal_dependencies.api.serializers import (
    NotaFiscalDependenciesSerializer, ItemNotaFiscalDependenciesSerializer
)
from notafiscal_dependencies.models import (
    NotaFiscalDependencies, ItemNotaFiscalDependencies
)

from notafiscal.util import Ferramentas


class NotaFiscalDependenciesViewset(viewsets.ModelViewSet):
    queryset = NotaFiscalDependencies.objects.all()
    serializer_class = NotaFiscalDependenciesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ultima_notafiscal = NotaFiscalDependencies.objects.all().last()
        numero_notafiscal = Ferramentas.gera_numero_notafiscal(ultima_notafiscal)
        serializer.validated_data.update({'numero': numero_notafiscal})

        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ItemNotaFiscalDependenciesViewset(viewsets.ModelViewSet):
    queryset = ItemNotaFiscalDependencies.objects.all()
    serializer_class = ItemNotaFiscalDependenciesSerializer
