from django import forms

class RegistrationForm(forms.Form):
    razao_social  = forms.CharField(max_length=100)
    nome_fantasia = forms.CharField(max_length=100)
    telefone = forms.CharField(max_length=100)
    cnpj = forms.CharField(max_length=100)
    endereco = forms.CharField(max_length=200)
    email = forms.CharField(max_length=100)