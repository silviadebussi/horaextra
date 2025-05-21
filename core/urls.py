from django.urls import path
from django.contrib.auth import views as auth_views
from core import views
from core.views import IndexView  # se usar classe-based view

urlpatterns = [
    # Landing page como página inicial
    path('', views.landing, name='landing'),

    # Página "inicio.html" (ex: dashboard ou home após login)
    path('inicio/', IndexView.as_view(), name='inicio'),

    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Registros de horas
    path('novo/', views.criar_registro, name='criar_registro'),
    path('lista/', views.lista_registros, name='lista_registros'),
    path('horas/', views.registrar_horas, name='registrar_horas'),

    # Atividades
    path('atividades/', views.listar_atividades, name='listar_atividades'),
    path('atividades/nova/', views.criar_atividade, name='criar_atividade'),
    path('atividades/editar/<int:pk>/', views.editar_atividade, name='editar_atividade'),
    path('atividades/excluir/<int:pk>/', views.excluir_atividade, name='excluir_atividade'),
    path('atividades/assumir/<int:atividade_id>/', views.assumir_atividade, name='assumir_atividade'),
    path('atividades/disponiveis/', views.atividades_disponiveis, name='atividades_disponiveis'),

    # Dashboard (separado da landing e da página inicio)
    path('dashboard/', views.dashboard, name='dashboard'),
]
