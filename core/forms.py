from django import forms
from .models import RegistroHora


from django import forms
from .models import RegistroHora, Regional, AtividadeHoraExtra
from django import forms
from .models import RegistroHora

class RegistroHoraForm(forms.ModelForm):
    class Meta:
        model = RegistroHora
        fields = ['regional', 'data', 'hora_inicio', 'hora_fim', 'descricao']
        widgets = {
            'regional': forms.Select(attrs={'class': 'form-select'}),  # Adiciona o Bootstrap para o campo select
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Campos com a classe form-control para input
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Adiciona form-control à descrição
        }


    regional = forms.ModelChoiceField(queryset=Regional.objects.all(), empty_label="Escolha a região")


class AtividadeHoraExtraForm(forms.ModelForm):
    class Meta:
        model = AtividadeHoraExtra
        fields = ['regional', 'descricao', 'data', 'hora_inicio', 'hora_fim']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'regional': forms.Select(attrs={'class': 'form-select'}),
        }
