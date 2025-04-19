from django import forms
from django.core.exceptions import ValidationError
from .models import FamiliasProduto

class FamiliaProdutoForm(forms.ModelForm):     

    class Meta:
        model = FamiliasProduto
        fields = ['descricao', 'produto']  # Ordem dos campos
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),           
        }
        labels = {
            'descricao': 'Descrição:',
            'produto': 'Produto:'
        }

    def clean(self):
        cleaned_data = super().clean()
        descricao = cleaned_data.get('descricao')
        produto = cleaned_data.get('produto')
            
        if descricao and produto:
                # Cria a consulta base para verificar duplicidade
            query = FamiliasProduto.objects.filter(descricao=descricao, produto=produto)
                
                # IMPORTANTE: Exclui o registro atual da verificação se estiver editando
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
                
                # Agora verifica se existe outro registro com o mesmo nome e CPF
            if query.exists():
                raise ValidationError("Já existe uma familia de produto cadastrada com estes dados.")
            
        return cleaned_data       

        