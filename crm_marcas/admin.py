from django.contrib import admin
from .models import Marcas

class MarcasAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'sigla', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('sigla',)
    list_filter = ('sigla',)
    ordering = ('-sigla',)

admin.site.register(Marcas, MarcasAdmin)
