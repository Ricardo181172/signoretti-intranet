from django import forms
from .models import Regioes, Culturas, AreasCultura
from django.core.exceptions import ValidationError
import datetime

class AreaCulturaForm(forms.ModelForm):
    
    class Meta:
        model = AreasCultura
        fields = ['ano', 'regiao', 'cultura', 'area']
        widgets = {
            'regiao': forms.Select(attrs={'class': 'form-control'}),
            'cultura': forms.Select(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'ano': 'Ano:',
            'regiao': 'Região:',
            'cultura': 'Cultura:',
            'area': 'Área:',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        ano = cleaned_data.get('ano')
        regiao = cleaned_data.get('regiao')
        cultura = cleaned_data.get('cultura')
        
        # Verifica se todos os campos necessários foram preenchidos
        if ano and regiao and cultura:
            # Consulta para verificar duplicidade
            query = AreasCultura.objects.filter(
                ano=ano,
                regiao=regiao,
                cultura=cultura
            )
            
            # Se estiver editando um registro existente, exclui ele mesmo da verificação
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
            
            # Verifica se já existe um registro com essa combinação
            if query.exists():
                raise ValidationError(
                    "Já existe uma área cadastrada para esta combinação de ano, região e cultura."
                )
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(AreaCulturaForm, self).__init__(*args, **kwargs)
        current_year = datetime.datetime.now().year
        self.fields['ano'] = forms.ChoiceField(
            choices=[(year, year) for year in range(current_year, current_year + 5)],
            widget=forms.Select(attrs={'class': 'form-control'}),
            label='Ano:'
        )
        
        self.fields['ano'].choices = [('', '---------')] + list(self.fields['ano'].choices)