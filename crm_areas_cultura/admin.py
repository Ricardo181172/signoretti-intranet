from django.contrib import admin
from .models import AreasCultura


class AreasCulturaAdmin(admin.ModelAdmin):
    list_display = ('ano', 
                  'regiao',
                  'cultura',
                  'area',
                  'data_criacao', 
                  'data_ultima_edicao')
    search_fields = ('regiao', 'cultura')
    list_filter = ('regiao', 'cultura')
    ordering = ('-regiao',)

admin.site.register(AreasCultura, AreasCulturaAdmin)