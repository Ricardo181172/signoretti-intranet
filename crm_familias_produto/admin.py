from django.contrib import admin
from .models import FamiliasProduto

class FamiliasProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'sigla', 'produto', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('descricao', 'sigla', 'produto')
    list_filter = ('descricao', 'sigla', 'produto')
    ordering = ('-sigla',)

admin.site.register(FamiliasProduto, FamiliasProdutoAdmin)
