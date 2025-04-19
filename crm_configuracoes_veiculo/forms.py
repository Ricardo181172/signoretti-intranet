from django import forms
from django.core.exceptions import ValidationError
from .models import ConfiguracoesVeiculo

class ConfiguracaoVeiculoForm(forms.ModelForm):

    class Meta:
        model = ConfiguracoesVeiculo
        fields = ['modelo', 'top_cat', 'acessorio']
        widgets = {            
            'modelo': forms.Select(attrs={'class': 'form-control'}),
            'acessorio': forms.Select(attrs={'class': 'form-control'}),
            'top_cat': forms.TextInput(attrs={'class': 'form-control'}),             
        }
        labels = {
            'modelo': 'Modelo', 
            'acessorio': 'Acessório',  
            'top_cat': 'Top Cat',                      
        }
    
    def clean(self):
            cleaned_data = super().clean()            
            top_cat = cleaned_data.get('top_cat')
            acessorio = cleaned_data.get('acessorio')
        
            if top_cat and acessorio:
            # Cria a consulta base para verificar duplicidade
                query = ConfiguracoesVeiculo.objects.filter(top_cat=top_cat, acessorio=acessorio)
            
            # IMPORTANTE: Exclui o registro atual da verificação se estiver editando
            if self.instance.pk:
                    query = query.exclude(pk=self.instance.pk)
            
            # Agora verifica se existe outro registro com o mesmo nome e CPF
            if query.exists():
                    raise ValidationError("Já existe um modelo com esse top cat e acessório.")
        
            return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        # Personalizar o texto da opção vazia para campos ModelChoiceField com "---------"
        self.fields['modelo'].empty_label = "---------"
        #self.fields['tipo_cliente'].choices = [('', '---------')] + list(self.fields['tipo_cliente'].choices)
        