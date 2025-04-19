from django.contrib import admin
from .models import PedidosVenda

class PedidosVendaAdmin(admin.ModelAdmin):
    list_display = ('emitente',
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
                    'status',
                    'observacoes',                    
                    'data_criacao', 
                    'data_ultima_edicao') 
    search_fields = ('emitente', 'cliente', 'veiculo')
    list_filter = ('emitente', 'cliente', 'veiculo')
    ordering = ('-emitente',)

admin.site.register(PedidosVenda, PedidosVendaAdmin)

    
   

