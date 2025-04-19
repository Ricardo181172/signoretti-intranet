from django.contrib import admin
from .models import AcessoriosVeiculo

class AcessoriosVeiculoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('-descricao',)

admin.site.register(AcessoriosVeiculo, AcessoriosVeiculoAdmin)
