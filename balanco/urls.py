from django.urls import path
from . import views

urlpatterns = [
    path('', views.balanco_patrimonial, name='balanco_patrimonial'),
    path('ativos/', views.ativos_listagem, name='ativos_listagem'),
    path('passivos/', views.passivos_listagem, name='passivos_listagem'),
    path('adicionar-ativo/', views.adicionar_ativo, name='adicionar_ativo'),
    path('adicionar-passivo/', views.adicionar_passivo, name='adicionar_passivo'),
]
