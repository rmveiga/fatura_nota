from rest_framework import routers

from entidade.api.viewsets import (
    EntidadeViewset, TelefoneViewset, EnderecoViewset
)

entidade_router = routers.DefaultRouter()
entidade_router.register('entidades', EntidadeViewset, basename='entidade-api')
entidade_router.register('telefones', TelefoneViewset, basename='telefone-api')
entidade_router.register('enderecos', EnderecoViewset, basename='endereco-api')