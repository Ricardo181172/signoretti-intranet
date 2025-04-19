from django import forms
from decimal import Decimal
from .models import PedidosVenda
from sis_bancos.models import Bancos
from crm_veiculos.models import Veiculos

class PedidoVendaForm(forms.ModelForm):
    STATUS_NEGOCIACAO_CHOICES = [
        ('', '---------'),  # Adicionando opção inicial vazia
        ('ABERTURA DE CREDITO', 'ABERTURA DE CREDITO'),
        ('VENDA C/ SINAL', 'VENDA C/ SINAL'),
        ('VENDA S/ SINAL', 'VENDA S/ SINAL'),
    ]

    status_negociacao = forms.ChoiceField(
        choices=STATUS_NEGOCIACAO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Status da Negociação:',
        required=False  # Tornando o campo não obrigatório
    )

    STATUS_FINANCIAMENTO_CHOICES = [
        ('', '---------'),  # Adicionando opção inicial vazia
        ('ANALISE', 'ANALISE'),
        ('APROVADO', 'APROVADO'),
        ('FATURADO', 'FATURADO'),
        ('MONTAGEM', 'MONTAGEM'),
        ('PAGO', 'PAGO'),
    ]

    status_financiamento = forms.ChoiceField(
        choices=STATUS_FINANCIAMENTO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Status do Financiamento:',
        required=False  # Tornando o campo não obrigatório
    )

    LINHA_CREDITO_CHOICES = [
        ('', '---------'),  # Adicionando opção inicial vazia
        ('FCO', 'FCO'),
        ('MAIS INOVAÇÃO', 'MAIS INOVAÇÃO'),
        ('MDA', 'MDA'),  
        ('TFBD', 'TFBD'),            
        ('OUTRA', 'OUTRA'),
    ]

    linha_credito = forms.ChoiceField(
        choices=LINHA_CREDITO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Linha de Crédito:',
        required=False  # Tornando o campo não obrigatório
    )

    banco = forms.ModelChoiceField(
        queryset=Bancos.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Banco:',
        required=False,
        empty_label='---------'  # Adicionando opção inicial vazia
    )
    
    valor = forms.DecimalField(
        label="Valor do Pedido:",
        widget=forms.TextInput(attrs={'class': 'form-control money-input', 'placeholder': '0,00'}),
        required=False  # Tornando o campo não obrigatório
    )

    outras_receitas = forms.DecimalField(
        label="Outras Receitas:",
        widget=forms.TextInput(attrs={'class': 'form-control money-input', 'placeholder': '0,00'}),
        required=False  # Tornando o campo não obrigatório
    ) 

    outras_despesas = forms.DecimalField(
        label="Outras Despesas:",
        widget=forms.TextInput(attrs={'class': 'form-control money-input', 'placeholder': '0,00'}),
        required=False  # Tornando o campo não obrigatório
    )         

    taxa_flat = forms.DecimalField(
        label="Taxa Flat:",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
        required=False  # Tornando o campo não obrigatório
    )

    porcent_financiamento = forms.IntegerField(
        label="Porcentagem de Financiamento:",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '100', 'placeholder': '0'}),
        required=False  # Tornando o campo não obrigatório
    )

    data_pedido = forms.DateField(
        label="Data do Pedido:",
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy', 'id': 'id_data_pedido'}, format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],
        required=False, 
    )

    data_envio_proposta = forms.DateField(
        label="Data de Envio da proposta:",
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy', 'id': 'id_envio_proposta'}, format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],
        required=False, 
    )

    data_aprovacao = forms.DateField(
        label="Data Aprovação:",
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy', 'id': 'id_data_aprovacao'}, format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],
        required=False, 
    )

    data_recebimento = forms.DateField(
        label="Data Recebimento:",
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/yyyy', 'id': 'id_data_recebimento'}, format='%d/%m/%Y'),
        input_formats=['%d/%m/%Y'],
        required=False, 
    )

    situacao_financiamento = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Digite a situação do financiamento aqui...'}),
        required=False  # Explicitamente não obrigatório
    )
    
    observacoes = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Digite suas observações aqui...'}),
        required=False  # Explicitamente não obrigatório
    )

    class Meta:
        model = PedidosVenda
        fields = [
            'emitente',
            'cliente', 
            'veiculo',
            'vendedor',
            'status_negociacao', 
            'status_financiamento',    
            'banco',
            'valor',
            'outras_receitas',
            'outras_despesas',
            'linha_credito',
            'taxa_flat',
            'porcent_financiamento',
            'data_pedido',
            'data_envio_proposta',
            'data_aprovacao',
            'data_recebimento',                    
            'situacao_financiamento',
            'observacoes'
        ]
        widgets = {            
            'emitente': forms.Select(attrs={'class': 'form-control'}),               
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'vendedor': forms.Select(attrs={'class': 'form-control'}),           
        }
        labels = {
            'emitente': 'Emitente:',
            'cliente': 'Cliente:',
            'veiculo': 'Veiculo:',
            'vendedor': 'Vendedor:',
            'status_negociacao': 'Status Negociação:',     
            'banco': 'Banco:',
            'valor_total': 'Valor:',
            'outras_receitas': 'Outras Receitas:',
            'outras_despesas': 'Outras Despesas:',
            'linha_credito': 'Linha Crédito:',
            'taxa_flat': 'Taxa Flat:',
            'porcent_financiamento': 'Financiamento:',
            'data_pedido': 'Data do Pedido:',
            'data_envio_proposta': 'Data Envio Proposta:',
            'data_aprovacao': 'Data Aprovação:',
            'data_recebimento': 'Data Recebimento:',                    
            'situacao_financiamento': 'Situação Financiamento:', 
            'observacoes': 'Observações:', 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filtrar APENAS veículos com situação "ESTOQUE"
        estoque_veiculos = Veiculos.objects.filter(situacao='ESTOQUE')
        
        # Atribuir diretamente a queryset filtrada ao campo
        self.fields['veiculo'].queryset = estoque_veiculos
        
        # Adicionar o veículo atual se estiver editando
        if self.instance and self.instance.pk and self.instance.veiculo:
            # Se o veículo atual não estiver na queryset, adicione-o
            if not estoque_veiculos.filter(pk=self.instance.veiculo.pk).exists():
                # Criar uma nova queryset combinando os veículos em estoque com o veículo atual
                self.fields['veiculo'].queryset = estoque_veiculos | Veiculos.objects.filter(pk=self.instance.veiculo.pk)
        
        # Resto do código para formatação de valores...
        if self.instance.pk:
            for field in ['valor', 'outras_receitas', 'outras_despesas']:
                value = getattr(self.instance, field)
                if value is not None:
                    self.initial[field] = f'{value:.2f}'.replace('.', ',')
        else:
            # Set initial/default values as 0,00
            for field in ['valor', 'outras_receitas', 'outras_despesas']:
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

    def clean_valor(self):
        return self.clean_money_field('valor')

    def clean_outras_receitas(self):
        return self.clean_money_field('outras_receitas')
    
    def clean_outras_despesas(self):
        return self.clean_money_field('outras_despesas')