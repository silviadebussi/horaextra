from django.views.generic import TemplateView
from .models import  Cliente, User, Regional, RegistroHora
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistroHoraForm

class IndexView(TemplateView):
    template_name = 'inicio.html'




@login_required
def lista_registros(request):
    registros = RegistroHora.objects.all()
    return render(request, 'core/lista_registros.html', {'registros': registros})

@login_required
def criar_registro(request):
    if request.method == 'POST':
        form = RegistroHoraForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.usuario = request.user
            registro.save()
            return redirect('lista_registros')
    else:
        form = RegistroHoraForm()
    return render(request, 'core/criar_registro.html', {'form': form})