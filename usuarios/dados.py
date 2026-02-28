from django import forms
from .models import Usuarios

class Dados(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['email', 'senha']

        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'input-login'
            }),
            'senha': forms.PasswordInput(attrs={
                'placeholder': 'Senha',
                'class': 'input-login'
            }),
        }

        labels = {
            'email': '',
            'senha': '',
        }