from django.contrib import admin
from .models import Modelos

class ModelosAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'sigla', 'cor', 'marca', 'familia_produto', 'custo_medio', 'venda_media', 'status', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('descricao', 'marca')
    list_filter = ('descricao', 'custo_medio', 'venda_media')
    ordering = ('-sigla',)

admin.site.register(Modelos, ModelosAdmin)
