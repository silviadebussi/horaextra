from django import forms
from .models import RegistroHora, Atividade
from django import forms
from .models import RegistroHora, Regional, AtividadeHoraExtra
from django import forms
from .models import RegistroHora

class RegistroHoraForm(forms.ModelForm):
    atividade = forms.ModelChoiceField(
        queryset=AtividadeHoraExtra.objects.filter(ocupada=False),
        label="Atividade",
        required=True
    )

    class Meta:
        model = RegistroHora
        fields = ['regional', 'data', 'hora_inicio', 'hora_fim', 'atividade']
        widgets = {
            'regional': forms.Select(attrs={'class': 'form-select'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
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
