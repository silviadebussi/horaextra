from django.contrib import admin
from .models import Cliente, Regional, RegistroHora, Atividade, RegistroHora, Perfil

admin.site.register(Cliente)
admin.site.register(Regional)
admin.site.register(RegistroHora)

admin.site.register(Atividade)
admin.site.register(Perfil)
