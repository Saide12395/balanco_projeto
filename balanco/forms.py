from django import forms
from .models import Ativo, Passivo

class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['nome', 'valor']

class PassivoForm(forms.ModelForm):
    class Meta:
        model = Passivo
        fields = ['nome', 'valor']
