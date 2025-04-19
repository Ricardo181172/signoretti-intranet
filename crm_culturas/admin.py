from django.contrib import admin
from .models import Culturas

class CulturasAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('-descricao',)

admin.site.register(Culturas, CulturasAdmin)
