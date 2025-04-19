from django import forms
from django.core.exceptions import ValidationError
from .models import CondicoesPagamento

class CondicaoPagamentoForm(forms.ModelForm):

    class Meta:
        model = CondicoesPagamento
        fields = ['descricao',]

        widgets = {            
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),            
        }
        labels = {
            'descricao': 'Descrição',            
        }
    
    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        
        # Cria a consulta para verificar duplicidade
        query = CondicoesPagamento.objects.filter(descricao=descricao)
        
        # Exclui o registro atual se estiver editando
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
            
        if query.exists():
            raise ValidationError('A condição de pagamento já está cadastrada. Por favor, escolha outra.')
            
        return descricao

