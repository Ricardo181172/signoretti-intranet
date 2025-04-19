from django import forms
from django.core.exceptions import ValidationError
from .models import Produtos


class ProdutoForm(forms.ModelForm):     

    class Meta:
        model = Produtos
        fields = ['descricao', 'sigla',]  # Ordem dos campos
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),            
        }

        labels = {
            'descricao': 'Descrição:',
            'sigla': 'Sigla:',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        descricao = cleaned_data.get('descricao')
        sigla = cleaned_data.get('sigla')
            
        if descricao and sigla:
                # Cria a consulta base para verificar duplicidade
            query = Produtos.objects.filter(descricao=descricao, sigla=sigla)
                
                # IMPORTANTE: Exclui o registro atual da verificação se estiver editando
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
                
                # Agora verifica se existe outro registro com o mesmo nome e CPF
            if query.exists():
                raise ValidationError("Já existe um produto cadastrado com estes dados.")
            
        return cleaned_data  