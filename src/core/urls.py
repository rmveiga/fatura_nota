"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from entidade.urls import entidade_router
from vendedor.urls import vendedor_router
from estoque.urls import estoque_router
from pedido_dependencies.urls import pedido_router

cadastros_router = routers.DefaultRouter()
cadastros_router.registry.extend(entidade_router.registry)
cadastros_router.registry.extend(vendedor_router.registry)

documentos_router = routers.DefaultRouter()
documentos_router.registry.extend(pedido_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cadastros/', include(cadastros_router.urls)),
    path('api/estoque/', include(estoque_router.urls)),
    path('api/documentos/', include(documentos_router.urls)),
]
