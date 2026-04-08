from django import forms
from .models import Usuarios


class Dados(forms.ModelForm):

    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuarios
        fields = ['email']