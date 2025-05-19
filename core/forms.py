from django import forms
from .models import RegistroHora


from django import forms
from .models import RegistroHora, Regional

class RegistroHoraForm(forms.ModelForm):
    class Meta:
        model = RegistroHora
        fields = ['regional', 'data', 'hora_inicio', 'hora_fim', 'descricao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }

    regional = forms.ModelChoiceField(queryset=Regional.objects.all(), empty_label="Escolha a região")

