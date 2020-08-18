from rest_framework import routers

from entidade.api.viewsets import EntidadeViewset

entidade_router = routers.DefaultRouter()
entidade_router.register('entidades', EntidadeViewset, basename='entidade-api')