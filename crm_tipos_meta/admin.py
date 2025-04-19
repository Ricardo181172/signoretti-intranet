from django.contrib import admin
from .models import TiposMeta

class TiposMetaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'status', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('-descricao',)

admin.site.register(TiposMeta, TiposMetaAdmin)

