from django import forms
from django.core.exceptions import ValidationError
from .models import AcessoriosVeiculo


class AcessorioVeiculoForm(forms.ModelForm):

    class Meta:
        model = AcessoriosVeiculo
        fields = ['descricao',]
        widgets = {            
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),            
        }
        
        labels = {
            'descricao': 'Descrição',            
        }
    
    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if AcessoriosVeiculo.objects.filter(descricao=descricao).exists():
            raise ValidationError('A descrição já está cadastrada. Por favor, escolha outra.')
        return descricao