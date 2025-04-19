from django import forms
from django.core.exceptions import ValidationError
from .models import Emitentes, Cidades

class EmitenteForm(forms.ModelForm):

    uf = forms.ChoiceField(
        choices=[('', 'Selecione um estado')] + [(uf, uf) for uf in Cidades.objects.values_list('uf', flat=True).distinct().order_by('uf')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Estado:'
    )

    class Meta:
        model = Emitentes
        fields = ['codigo', 'nome', 'uf', 'cidade']
        widgets = {
            'codigo': forms.NumberInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'codigo': 'Código',
            'nome': 'Loja',
            'cidade': 'Cidade',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        codigo = cleaned_data.get('codigo')
        nome = cleaned_data.get('nome')
        cidade = cleaned_data.get('cidade')
        
        # Verifica se todos os campos necessários foram preenchidos
        if codigo and nome and cidade:
            # Consulta para verificar duplicidade
            query = Emitentes.objects.filter(
                codigo=codigo,
                nome=nome,
                cidade=cidade
            )
            
            # Se estiver editando um registro existente, exclui ele mesmo da verificação
            if self.instance.pk:
                query = query.exclude(pk=self.instance.pk)
            
            # Verifica se já existe um registro com essa combinação
            if query.exists():
                raise ValidationError(
                    "Já existe uma região para esta combinação de região e cidade."
                )
        
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