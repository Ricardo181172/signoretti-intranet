from django.contrib import admin
from .models import Produtos

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'sigla', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('descricao', 'sigla')
    list_filter = ('descricao', 'sigla')
    ordering = ('-sigla',)

admin.site.register(Produtos, ProdutosAdmin)
