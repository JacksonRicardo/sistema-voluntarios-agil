from django import forms
from .models import Voluntario

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome_completo', 'cpf', 'data_nascimento', 'email', 'telefone', 'area_atuacao', 'experiencia']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'placeholder': 'Digite seu nome completo'}),
            'cpf': forms.TextInput(attrs={'placeholder': '000.000.000-00'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}), 
            'email': forms.EmailInput(attrs={'placeholder': 'exemplo@email.com'}),
            'telefone': forms.TextInput(attrs={'placeholder': '(00) 00000-0000'}),
            'experiencia': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Resuma suas habilidades...'}),
        }
