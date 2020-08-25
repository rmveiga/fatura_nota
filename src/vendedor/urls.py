from rest_framework import routers

from vendedor.api.viewsets import VendedorViewset

vendedor_router = routers.DefaultRouter()
vendedor_router.register('vendedores', VendedorViewset, basename='vendedor-api')

