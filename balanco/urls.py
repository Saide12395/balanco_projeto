from django.urls import path
from . import views

urlpatterns = [
    path('', views.balanco_patrimonial, name='balanco_patrimonial'),
    path('ativos/', views.ativos_listagem, name='ativos_listagem'),
    path('adicionar-ativo/', views.adicionar_ativo, name='adicionar_ativo'),
    path('editar-ativo/<int:ativo_id>/', views.editar_ativo, name='editar_ativo'),
    path('apagar-ativo/<int:ativo_id>/', views.apagar_ativo, name='apagar_ativo'),
    path('passivos/', views.passivos_listagem, name='passivos_listagem'),
    path('adicionar-passivo/', views.adicionar_passivo, name='adicionar_passivo'),
    path('editar-passivo/<int:passivo_id>/', views.editar_passivo, name='editar_passivo'),
    path('apagar-passivo/<int:passivo_id>/', views.apagar_passivo, name='apagar_passivo'),
]
