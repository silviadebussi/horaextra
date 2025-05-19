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

]