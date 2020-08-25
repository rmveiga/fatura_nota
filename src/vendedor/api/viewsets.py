from rest_framework import viewsets

from vendedor.api.serializers import VendedorSerializer
from vendedor.models import Vendedor


class VendedorViewset(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

