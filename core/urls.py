from django.urls import path
from .views import (
    IndexView,
)

from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("inicio.html", IndexView.as_view(), name="inicio"),
    path('', views.lista_registros, name='lista_registros'),
    path('novo/', views.criar_registro, name='criar_registro'),
    path('atividades/', views.atividades_disponiveis, name='atividades_disponiveis'),
    path('atividades/assumir/<int:atividade_id>/', views.assumir_atividade, name='assumir_atividade'),

]