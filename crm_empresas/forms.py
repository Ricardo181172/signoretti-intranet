from django import forms
from django.core.exceptions import ValidationError
from .models import Empresas, Cidades

class EmpresasForm(forms.ModelForm):

    TIPO_EMPRESA_CHOICES = [
        ('PUBLICA', 'PUBLICA'),
        ('CONCORRENTE', 'CONCORRENTE'),
        ('PRIVADA', 'PRIVADA'),
        ('REDE NH', 'REDE NH'),
        ('REDE JD', 'REDE JD'),
    ]

    tipo_empresa = forms.ChoiceField(
        choices=TIPO_EMPRESA_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Tipo Empresa:'
    )
    
    uf = forms.ChoiceField(
        choices=[('', 'Selecione um estado')] + [(uf, uf) for uf in Cidades.objects.values_list('uf', flat=True).distinct().order_by('uf')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Estado:'
    )

    class Meta:
        model = Empresas
        fields = ['nome', 'tipo_empresa', 'uf', 'cidade']  # Ordem dos campos
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_empresa': forms.Select(attrs={'class': 'form-control'}),           
            'cidade': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome:', 
            'tipo_empresa': 'Tipo Empresa:',
            'cidade': 'Cidade:',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        tipo_empresa = cleaned_data.get('tipo_empresa')
        cidade = cleaned_data.get('cidade')
        
        if nome and tipo_empresa and cidade:
            # Cria a consulta base para verificar duplicidade
            query = Empresas.objects.filter(nome=nome, tipo_empresa=tipo_empresa, cidade=cidade)
            
            # IMPORTANTE: Exclui o registro atual da verificação se estiver editando
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
            
            # Agora verifica se existe outro registro com o mesmo nome e CPF
            if query.exists():
                raise ValidationError("Já existe uma empresa cadastrada com os mesmos dados.")
        
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cidade'].queryset = Cidades.objects.none()        

        if 'uf' in self.data:
            uf = self.data.get('uf')
            if uf:
                self.fields['cidade'].queryset = Cidades.objects.filter(uf=uf).order_by('municipio')
        elif self.instance.pk:
            self.fields['uf'].initial = self.instance.cidade.uf
            self.fields['cidade'].queryset = Cidades.objects.filter(uf=self.instance.cidade.uf).order_by('municipio')

        # Personalizar o texto de exibição das opções de cidade
        if self.fields['cidade'].queryset:
            self.fields['cidade'].choices = [
                (cidade.id, cidade.municipio) for cidade in self.fields['cidade'].queryset
            ]
        
        self.fields['tipo_empresa'].choices = [('', '---------')] + list(self.fields['tipo_empresa'].choices)
        