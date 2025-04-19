from django import forms
from django.core.exceptions import ValidationError
from .models import Impostos

class ImpostoForm(forms.ModelForm):

    class Meta:
        model = Impostos
        fields = ['descricao', 'incidencia', 'taxa']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'incidencia': forms.TextInput(attrs={'class': 'form-control'}),
            'taxa': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01',  # Permite incrementos de 0.01, ou seja, precisão de duas casas decimais
                    'min': '0',      # Define o valor mínimo se aplicável
                    'max': '100'     # Considerando que é uma porcentagem, limita a entrada até 100
                }
            ),
        }

        labels = {
            'descricao': 'Descrição',
            'incidencia': 'Incidência',
            'taxa': 'Taxa',
        }

    def clean(self):
        cleaned_data = super().clean()
        descricao = cleaned_data.get('descricao')
        incidencia = cleaned_data.get('incidencia')        
            
        if descricao and incidencia:
                # Cria a consulta base para verificar duplicidade
            query = Impostos.objects.filter(descricao=descricao, incidencia=incidencia)
                
                # IMPORTANTE: Exclui o registro atual da verificação se estiver editando
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
                
                # Agora verifica se existe outro registro com o mesmo nome e CPF
            if query.exists():
                raise ValidationError("Já existe um imposto cadastrado com estes dados.")
            
        return cleaned_data   