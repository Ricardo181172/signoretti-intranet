from django import forms
from decimal import Decimal
from django.core.exceptions import ValidationError
from .models import Veiculos

class VeiculoForm(forms.ModelForm):

    ESTADO_CHOICES = [
        ('', '---------'),
        ('NOVO', 'NOVO'),
        ('USADO', 'USADO'),
    ]

    estado = forms.ChoiceField(
        choices=ESTADO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Estado:'
    )

    SITUACAO_CHOICES = [
        ('', '---------'),
        ('ESTOQUE', 'ESTOQUE'),
        ('EM PEDIDO', 'EM PEDIDO'),
        ('FATURADO S/R', 'FATURADO S/R'),
        ('FÁBRICA', 'FÁBRICA'),        
        ('VENDIDO', 'VENDIDO'),
    ]

    situacao = forms.ChoiceField(
        choices=SITUACAO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Situação:'
    )

    data_compra = forms.DateField(
        label="Data Compra:",
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy', 'id': 'id_data_compra'}, format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],
        required=False, 
    )

    data_quitacao = forms.DateField(
        label="Data Quitação:",
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy', 'id': 'id_data_quitacao'}, format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],
        required=False, 
    )

    valor_custo = forms.DecimalField(
        label="Valor Custo:",
        widget=forms.TextInput(attrs={'class': 'form-control money-input', 'placeholder': '0,00'}),
        required=False,        
    )  

    valor_venda = forms.DecimalField(
        label="Valor Venda:",
        widget=forms.TextInput(attrs={'class': 'form-control money-input', 'placeholder': '0,00'}),
        required=False,               
    )        

    class Meta:
        model = Veiculos
        fields = ['emitente', 'estado', 'modelo', 'acessorio_veiculo', 'prazo_free', 'serie', 'chassi', 'valor_custo', 'valor_venda', 'situacao', 'data_compra', 'data_quitacao', 'nf_compra', 'nf_venda']
        widgets = {            
            'emitente': forms.Select(attrs={'class': 'form-control'}), 
            'modelo': forms.Select(attrs={'class': 'form-control'}), 
            'acessorio_veiculo': forms.Select(attrs={'class': 'form-control'}), 
            'prazo_free': forms.NumberInput(attrs={'class': 'form-control'}),         
            'serie': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_celular'}),
            'chassi': forms.TextInput(attrs={'class': 'form-control'}),
            'nf_compra': forms.NumberInput(attrs={'class': 'form-control'}),    
            'nf_venda': forms.NumberInput(attrs={'class': 'form-control'}),    
        }
        labels = {
            'emitente': 'Emitente:',
            'estado': 'Estado:',
            'modelo': 'Modelo:',
            'acessorio_veiculo': 'Configuração do Veiculo:',
            'prazo_free': 'Prazo Free:',
            'serie': 'Série:',
            'chassi': 'Chassi:',
            'valor_custo': 'Valor de Custo:',
            'valor_venda': 'Valor de Custo:',
            'situacao': 'Situação:',
            'data_compra': 'Data da Compra:',
            'nf_compra': 'NF de Compra:',
            'nf_venda': 'NF de Venda:',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            for field in ['valor_custo', 'valor_venda']:
                value = getattr(self.instance, field)
                if value is not None:
                    self.initial[field] = f'{value:.2f}'.replace('.', ',')
        else:
            # Set initial/default values as 0,00
            for field in ['valor_custo', 'valor_venda']:
                self.initial.setdefault(field, '0,00')


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
    
    def clean_valor_custo(self):
        return self.clean_money_field('valor_custo')
    
    def clean_valor_venda(self):
        return self.clean_money_field('valor_venda')
