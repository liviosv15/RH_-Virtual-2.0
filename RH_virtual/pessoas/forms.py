from django import forms 
from .models import Pessoas 

class cadastroPessoa(forms.ModelForm):
    class Meta:
        model = Pessoas 
        fields = ('nome', 'sobrenome','email_login', 'senha_login')
