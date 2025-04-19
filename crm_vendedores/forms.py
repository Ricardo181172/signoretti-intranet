from django import forms
from .models import Vendedores

class VendedorForm(forms.ModelForm):    

    class Meta:
        model = Vendedores
        fields = ['nome', 'sobrenome', 'emitente', 'e_mail', 'celular', 'usuario_crm', 'senha_crm']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
            'emitente': forms.Select(attrs={'class': 'form-control'}),            
            'e_mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_celular'}),
            'usuario_crm': forms.TextInput(attrs={'class': 'form-control'}),
            'senha_crm': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'codigo': 'Código:',
            'nome': 'Nome:',
            'sobrenome': 'Sobrenome:',
            'emitente': 'Loja:',
            'e_mail': 'E-mail:',
            'celular': 'Celular:',
            'usuario_crm': 'Usuário CRM:',
            'senha_crm': 'Senha CRM:',
        }
