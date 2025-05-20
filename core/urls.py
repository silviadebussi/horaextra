from django.urls import path
from .views import (
    IndexView,
)

from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from core.views import listar_atividades

urlpatterns = [
    path("inicio.html", IndexView.as_view(), name="inicio"),
    path('', views.lista_registros, name='lista_registros'),
    path('atividades/', views.listar_atividades, name='lista_atividades'),
    path('novo/', views.criar_registro, name='criar_registro'),
    path('atividades/', views.atividades_disponiveis, name='atividades_disponiveis'),
    path('atividades/assumir/<int:atividade_id>/', views.assumir_atividade, name='assumir_atividade'),
    path('atividades/', views.listar_atividades, name='listar_atividades'),
    path('atividades/nova/', views.criar_atividade, name='criar_atividade'),
    path('atividades/editar/<int:pk>/', views.editar_atividade, name='editar_atividade'),
    path('atividades/excluir/<int:pk>/', views.excluir_atividade, name='excluir_atividade'),

]