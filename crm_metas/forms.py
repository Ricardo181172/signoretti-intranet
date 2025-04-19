from django import forms
from django.core.exceptions import ValidationError
from decimal import Decimal
import datetime
from .models import Metas

class MetaForm(forms.ModelForm):

    valor = forms.DecimalField(
        label="Valor",
        widget=forms.TextInput(attrs={'class': 'form-control money-input', 'placeholder': '0,00'})
    )    

    class Meta:
        model = Metas
        fields = ['mes', 'ano', 'tipo_meta', 'vendedor', 'produto', 'valor', 'quantidade']
        widgets = {
            'mes': forms.Select(choices=[(i, f"{i:02}") for i in range(1, 13)], attrs={'class': 'form-control'}),            
            'tipo_meta': forms.Select(attrs={'class': 'form-control'}),               
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.Select(attrs={'class': 'form-control'}),  
                     
        }
        labels = {
            'mes': 'Mês:',
            'ano': 'Ano:',
            'tipo_meta': 'Tipo da Meta:',
            'vendedor': 'Vendedor:',
            'produto': 'Produto:',
            'valor': 'Valor:',
            'quantiade': 'Quantidade:',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_year = datetime.datetime.now().year
        self.fields['ano'] = forms.ChoiceField(
            choices=[(year, year) for year in range(current_year, current_year + 5)],
            widget=forms.Select(attrs={'class': 'form-control'}),
            label='Ano:'
        )

        if self.instance.pk:
            for field in ['valor']:
                value = getattr(self.instance, field)
                if value is not None:
                    self.initial[field] = f'{value:.2f}'.replace('.', ',')
                    
        self.fields['ano'].choices = [('', '---------')] + list(self.fields['ano'].choices)

    def clean(self):
        cleaned_data = super().clean()
        mes = cleaned_data.get('mes')
        ano = cleaned_data.get('ano') 
        tipo_meta = cleaned_data.get('tipo_meta')
        vendedor = cleaned_data.get('vendedor') 
        produto = cleaned_data.get('produto') 
            
        if mes and ano and tipo_meta and vendedor and produto:
                # Cria a consulta base para verificar duplicidade
            query = Metas.objects.filter(mes=mes, ano=ano, tipo_meta=tipo_meta, vendedor=vendedor, produto=produto)
                
                # IMPORTANTE: Exclui o registro atual da verificação se estiver editando
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
                
                # Agora verifica se existe outro registro com o mesmo nome e CPF
            if query.exists():
                raise ValidationError("Já existe uma meta cadastrada com estes dados.")
            
        return cleaned_data

    def clean_valor(self):
        return self.clean_money_field('valor')

    def clean_money_field(self, field_name):
        value = self.cleaned_data.get(field_name)
        if isinstance(value, str):
            value = value.replace('R$', '').replace('.', '').replace(',', '.')
        try:
            return Decimal(value)
        except:
            raise forms.ValidationError(f"Por favor, insira um valor válido para {field_name}.")
        
    