from django import forms
from .models import Vendas

class VendaForm(forms.ModelForm):    

    class Meta:
        model = Vendas
        fields = ['pedido_venda', 'nf_venda']
        
        widgets = {
            'pedido_venda': forms.Select(attrs={'class': 'form-control'}),            
            'nf_venda': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'pedido_venda': 'Pedido de Venda:',
            'nf_venda': 'Nota Fiscal de Venda:',
        }
