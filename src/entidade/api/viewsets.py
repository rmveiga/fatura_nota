from rest_framework import viewsets

from entidade.api.serializers import EntidadeSerializer
from entidade.models import Entidade

class EntidadeViewset(viewsets.ModelViewSet):
    queryset = Entidade.objects.all()
    serializer_class = EntidadeSerializer