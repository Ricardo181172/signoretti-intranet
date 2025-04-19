from django import forms
from django.core.exceptions import ValidationError
from .models import TiposComissao

class TipoComissaoForm(forms.ModelForm):

    class Meta:
        model = TiposComissao
        fields = ['descricao',]
        widgets = {            
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),            
        }

        labels = {
            'descricao': 'Descrição',            
        }

    def clean(self):
        cleaned_data = super().clean()
        descricao = cleaned_data.get('descricao')
        
        if descricao:
            # Cria a consulta para verificar duplicidade
            query = TiposComissao.objects.filter(descricao__iexact=descricao)
            
            # Exclui o registro atual se estiver editando
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
                
            if query.exists():
                self.add_error('descricao', 'O tipo de comissão já está cadastrado. Por favor, escolha outro.')
        
        return cleaned_data 
