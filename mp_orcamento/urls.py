from django.urls import path
from .views import *

urlpatterns = [
    path('orcamentos/', orcamentos_lista, name='orcamentos-lista'),
    path('orcamentos/estatisticas/', orcamentos_estatisticas, name='orcamentos-estatisticas'),
    path('cliente/', primeiro_cliente, name='primeiro-clientes'),
    path('cliente/estatisticas/', cliente_estatisticas, name='estatisticas-cliente'),
]
