from django.contrib import admin
from .models import Clientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('emitente',
                    'nome', 
                    'cidade',
                    'vendedor',
                    'categoria',                    
                    'cpf_cnpj',
                    'tipo_cliente',
                    'e_mail',
                    'frota_ativa',
                    'frota_total',
                    'latitude',
                    'longitude',                    
                    'status',
                    'data_criacao', 
                    'data_ultima_edicao')
    search_fields = ('emitente', 'nome', 'cpf_cnpj', 'cidade')
    list_filter = ('emitente', 'nome', 'cpf_cnpj', 'cidade')
    ordering = ('-emitente',)
