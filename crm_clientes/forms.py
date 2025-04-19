from django import forms
from django.core.exceptions import ValidationError
from .models import Clientes, Cidades
from sis_emitentes.models import Emitentes

class ClienteForm(forms.ModelForm):
    TIPO_CLIENTE_CHOICES = [
        ('FISICA', 'FISICA'),
        ('JURIDICA', 'JURIDICA'),
    ]

    tipo_cliente = forms.ChoiceField(
        choices=TIPO_CLIENTE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tipo Cliente:'
    )

    CARTEGORIA_CHOICES = [
        ('CLIENTE CHAVE', 'CLIENTE CHAVE'),
        ('GOVERNO', 'GOVERNO'),
        ('TOP', 'TOP'),
        ('VAREJO', 'VAREJO'),        
    ]

    categoria = forms.ChoiceField(
        choices=CARTEGORIA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Categoria:'
    )

    STATUS_CHOICES = [
        ('COM RELACIONAMENTO', 'COM RELACIONAMENTO'),
        ('NOVO', 'NOVO'),
        ('SEM RELACIONAMENTO', 'SEM RELACIONAMENTO'),
    ]

    status_relacionamento = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Status Relacionamento:'
    )

    INDICADOR_CHOICES = [
        ('INDIFERENTE COM A MARCA', 'INDIFERENTE COM A MARCA'),
        ('INSATISFEITO COM A MARCA', 'INSATISFEITO COM A MARCA'),
        ('MUITO INSATISFEITO, NÃO PRETENDE VOLTAR PARA A MARCA', 'MUITO INSATISFEITO, NÃO PRETENDE VOLTAR PARA A MARCA'),
        ('SATISFEITO COM A MARCA', 'SATISFEITO COM A MARCA'),
        ('NÃO INFORMADO', 'NÃO INFORMADO'),
    ]

    indicador_temperatura = forms.ChoiceField(
        choices=INDICADOR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Indicador de Temperatura:'
    )

    uf = forms.ChoiceField(
        choices=[('', '---------')] + [(uf, uf) for uf in Cidades.objects.values_list('uf', flat=True).distinct().order_by('uf')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Estado:'
    )

    class Meta:
        model = Clientes
        fields = ['emitente', 'nome', 'uf', 'cidade', 'tipo_cliente', 'cpf_cnpj', 'vendedor', 'celular',  'e_mail', 'frota_total', 'frota_ativa', 'area_plantada', 'status_relacionamento', 'indicador_temperatura', 'categoria', 'latitude', 'longitude']

        widgets = {
            'emitente': forms.Select(attrs={'class': 'form-control'}),            
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'tipo_cliente': forms.Select(attrs={'class': 'form-control'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'vendedor': forms.Select(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_celular'}),
            'e_mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'frota_total': forms.NumberInput(attrs={'class': 'form-control'}),   
            'frota_ativa': forms.NumberInput(attrs={'class': 'form-control'}),   
            'area_plantada': forms.NumberInput(attrs={'class': 'form-control'}),   
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),   
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),               
        }
        labels = {
            'emitente': 'Emitente:',
            'nome': 'Nome:',
            'sobrenome': 'Sobrenome:',
            'tipo_cliente': 'Tipo do Cliente:',
            'cpf_cnpj': 'CPF/CNPJ:',
            'cidade': 'Cidade:',
            'vendedor': 'Vendedor:',
            'celular': 'Celular:',
            'e_mail': 'E-mail:',
            'frota_ativa': 'Frota Ativa:',
            'frota_total': 'Frota Total:',
            'area_plantada': 'Área Plantada:',
            'latitude': 'Latitude:',
            'longitude': 'Longitude:',
        }

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        cpf_cnpj = cleaned_data.get('cpf_cnpj')
        
        if nome and cpf_cnpj:
            # Cria a consulta base para verificar duplicidade
            query = Clientes.objects.filter(nome=nome, cpf_cnpj=cpf_cnpj)
            
            # IMPORTANTE: Exclui o registro atual da verificação se estiver editando
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
            
            # Agora verifica se existe outro registro com o mesmo nome e CPF
            if query.exists():
                raise ValidationError("Já existe uma pessoa cadastrada com este nome e CPF.")
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['celular'].required = False
        self.fields['e_mail'].required = False
        self.fields['latitude'].required = False
        self.fields['longitude'].required = False
        
        # Personalizar o texto da opção vazia para campos ModelChoiceField com "---------"
        self.fields['emitente'].empty_label = "---------"
        self.fields['uf'].empty_label = "Selecione um Estado"        
        self.fields['cidade'].empty_label = "---------"
        self.fields['tipo_cliente'].choices = [('', '---------')] + list(self.fields['tipo_cliente'].choices)
        self.fields['vendedor'].empty_label = "---------"
        self.fields['status_relacionamento'].choices = [('', '---------')] + list(self.fields['status_relacionamento'].choices)
        self.fields['indicador_temperatura'].choices = [('', '---------')] + list(self.fields['indicador_temperatura'].choices)
        self.fields['categoria'].choices = [('', '---------')] + list(self.fields['categoria'].choices)

        # Configuração do campo cidade baseado no estado selecionado
        self.fields['cidade'].queryset = Cidades.objects.none()

        if 'uf' in self.data:
            uf = self.data.get('uf')
            if uf:
                self.fields['cidade'].queryset = Cidades.objects.filter(uf=uf).order_by('municipio')
        elif self.instance.pk and hasattr(self.instance, 'cidade') and self.instance.cidade:
            self.fields['uf'].initial = self.instance.cidade.uf
            self.fields['cidade'].queryset = Cidades.objects.filter(uf=self.instance.cidade.uf).order_by('municipio')
        
        # Personalizar o texto de exibição das opções de cidade
        if self.fields['cidade'].queryset:
            self.fields['cidade'].choices = [
                (cidade.id, cidade.municipio) for cidade in self.fields['cidade'].queryset
            ]