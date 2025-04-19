from django.contrib import admin
from .models import ConfiguracoesVeiculo

class ConfiguracoesVeiculoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'modelo', 'top_cat', 'acessorio', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('descricao', 'modelo', 'acessorio')
    list_filter = ('descricao', 'modelo', 'acessorio')
    ordering = ('-modelo',)

admin.site.register(ConfiguracoesVeiculo, ConfiguracoesVeiculoAdmin)
