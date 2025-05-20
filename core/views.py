from django.views.generic import TemplateView
from .models import Cliente, User, Regional, RegistroHora, AtividadeHoraExtra, Perfil, Atividade
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistroHoraForm
from .models import AtividadeHoraExtra
from .forms import AtividadeHoraExtraForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


class IndexView(TemplateView):
    template_name = 'inicio.html'


@login_required
def dashboard(request):
    perfil = Perfil.objects.get(usuario=request.user)
    if perfil.tipo == 'gestor':
        return redirect('lista_atividades')
    else:
        return redirect('registrar_horas')

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

@login_required
def atividades_disponiveis(request):
    perfil = request.user.perfil
    atividades = AtividadeHoraExtra.objects.filter(ocupada=False, regional=perfil.regional)
    return render(request, 'core/atividades_disponiveis.html', {'atividades': atividades})

@login_required
def assumir_atividade(request, atividade_id):
    atividade = get_object_or_404(AtividadeHoraExtra, id=atividade_id, ocupada=False)

    atividade.ocupada = True
    atividade.funcionario = request.user
    atividade.save()


    RegistroHora.objects.create(
        regional=atividade.regional,
        data=atividade.data,
        hora_inicio=atividade.hora_inicio,
        hora_fim=atividade.hora_fim,
        descricao=atividade.descricao
    )

    return redirect('atividades_disponiveis')


def gestor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not hasattr(request.user, 'perfil') or request.user.perfil.tipo != 'gestor':
            return HttpResponseForbidden("Apenas gestores têm acesso.")
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
@gestor_required
def listar_atividades(request):
    atividades = AtividadeHoraExtra.objects.filter(gestor=request.user)
    return render(request, 'core/atividades/listar.html', {'atividades': atividades})

@login_required
@gestor_required
def criar_atividade(request):
    if request.method == 'POST':
        form = AtividadeHoraExtraForm(request.POST)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.gestor = request.user
            atividade.save()
            return redirect('listar_atividades')
    else:
        form = AtividadeHoraExtraForm()
    return render(request, 'core/atividades/form.html', {'form': form})

@login_required
@gestor_required
def editar_atividade(request, pk):
    atividade = get_object_or_404(AtividadeHoraExtra, pk=pk, gestor=request.user)
    if request.method == 'POST':
        form = AtividadeHoraExtraForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect('listar_atividades')
    else:
        form = AtividadeHoraExtraForm(instance=atividade)
    return render(request, 'core/atividades/form.html', {'form': form})

@login_required
@gestor_required
def excluir_atividade(request, pk):
    atividade = get_object_or_404(AtividadeHoraExtra, pk=pk, gestor=request.user)
    if request.method == 'POST':
        atividade.delete()
        return redirect('listar_atividades')
    return render(request, 'core/atividades/confirmar_exclusao.html', {'atividade': atividade})


@login_required
def registrar_horas(request):
    perfil = Perfil.objects.get(usuario=request.user)
    if perfil.tipo != 'funcionario':
        return redirect('lista_atividades')
    if request.method == 'POST':
        form = RegistroHoraForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.funcionario = request.user
            registro.save()
            return redirect('registrar_horas')
    else:
        form = RegistroHoraForm()
        form.fields['atividade'].queryset = Atividade.objects.filter(disponivel=True)
    return render(request, 'horas/form.html', {'form': form})


@login_required
def painel(request):
    return render(request, 'inicio.html')
