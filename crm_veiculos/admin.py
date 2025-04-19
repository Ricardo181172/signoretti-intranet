from django.contrib import admin
from .models import Veiculos

class VeiculosAdmin(admin.ModelAdmin):
    list_display = ('emitente',
                    'estado',
                    'modelo', 
                    'acessorio_veiculo',
                    'prazo_free',                       
                    'serie',                      
                    'chassi',
                    'valor_custo',
                    'valor_venda', 
                    'situacao',
                    'data_compra',                       
                    'data_pedido',
                    'data_quitacao',                      
                    'data_venda',
                    'nf_compra',
                    'nf_venda',
                    'status',
                    'data_criacao', 
                    'data_ultima_edicao') 
    search_fields = ('emitente', 'modelo', 'acessorio_veiculo')
    list_filter = ('emitente', 'modelo', 'acessorio_veiculo')
    ordering = ('-emitente',)

admin.site.register(Veiculos, VeiculosAdmin)
