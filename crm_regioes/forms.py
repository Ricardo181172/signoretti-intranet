from django import forms
from django.core.exceptions import ValidationError
from .models import Regioes


class RegiaoForm(forms.ModelForm):

    class Meta:
        model = Regioes
        fields = ['descricao',]
        widgets = {            
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),            
        }

        labels = {
            'descricao': 'Descrição',            
        }

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if Regioes.objects.filter(descricao=descricao).exists():
            raise ValidationError('A região já está cadastrada. Por favor, escolha outra.')
        return descricao
       
