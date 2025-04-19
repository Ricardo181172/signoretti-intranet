from django.contrib import admin
from .models import Impostos

class ImpostosAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'incidencia', 'taxa', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('descricao', 'incidencia', 'taxa')
    list_filter = ('descricao', 'incidencia', 'taxa')
    ordering = ('-descricao',)

admin.site.register(Impostos, ImpostosAdmin)   
