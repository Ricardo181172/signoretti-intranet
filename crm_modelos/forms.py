from django import forms
from decimal import Decimal
from django.core.exceptions import ValidationError
from .models import Modelos

class ModeloForm(forms.ModelForm):
    COR_CHOICES = [
        ('AMARELO', 'AMARELO'),
        ('AZUL', 'AZUL'),
        ('BRANCO', 'BRANCO'),
        ('LARANJA', 'LARANJA'),        
        ('PRETO', 'PRETO'),
        ('VERDE', 'VERDE'),
        ('VERMELHO', 'VERMELHO'),        
    ]

    cor = forms.ChoiceField(
        choices=COR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Cor:'
    )

    custo_medio = forms.DecimalField(
        label="Custo Médio",
        widget=forms.TextInput(attrs={'class': 'form-control money-input', 'placeholder': '0,00'}),
        required=False, 
    )
    venda_media = forms.DecimalField(
        label="Venda Média",
        widget=forms.TextInput(attrs={'class': 'form-control money-input', 'placeholder': '0,00'}),
        required=False, 
    )

    class Meta:
        model = Modelos
        fields = ['descricao', 'marca', 'cor', 'familia_produto', 'custo_medio', 'venda_media']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}), 
            'marca': forms.Select(attrs={'class': 'form-control'}),           
            'familia_produto': forms.Select(attrs={'class': 'form-control'}),           
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            for field in ['venda_media', 'custo_medio']:
                value = getattr(self.instance, field)
                if value is not None:
                    self.initial[field] = f'{value:.2f}'.replace('.', ',')
        else:
            # Set initial/default values as 0,00
            for field in ['venda_media', 'custo_medio']:
                self.initial.setdefault(field, '0,00')

        self.fields['cor'].choices = [('', '---------')] + list(self.fields['cor'].choices)

    def clean_money_field(self, field_name):
        value = self.cleaned_data.get(field_name)
        
        # If value is None or empty, set it to 0.00
        if not value:
            return Decimal('0.00')
        
        if isinstance(value, str):
            value = value.replace('R$', '').replace('.', '').replace(',', '.')
        
        try:
            return Decimal(value)
        except:
            raise forms.ValidationError(f"Por favor, insira um valor válido para {field_name}.")

    def clean_custo_medio(self):
        return self.clean_money_field('custo_medio')

    def clean_venda_media(self):
        return self.clean_money_field('venda_media')   
        
    def clean(self):
        cleaned_data = super().clean()
        descricao = cleaned_data.get('descricao')
        marca = cleaned_data.get('marca')
        familia_produto = cleaned_data.get('familia_produto')
            
        if descricao and marca and familia_produto:
                # Cria a consulta base para verificar duplicidade
            query = Modelos.objects.filter(descricao=descricao, marca=marca, familia_produto=familia_produto)
                
                # IMPORTANTE: Exclui o registro atual da verificação se estiver editando
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
                
                # Agora verifica se existe outro registro com o mesmo nome e CPF
            if query.exists():
                raise ValidationError("Já existe uma marca cadastrada com estes dados.")
            
        return cleaned_data  
