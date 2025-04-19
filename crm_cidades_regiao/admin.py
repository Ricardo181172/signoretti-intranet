from django.contrib import admin
from .models import CidadesRegiao

class CidadesRegiaoAdmin(admin.ModelAdmin):
    list_display = ('regiao', 
                  'cidade',                  
                  'status',
                  'data_criacao', 
                  'data_ultima_edicao')
    search_fields = ('regiao', 'cidade',)
    list_filter = ('regiao', 'cidade',)
    ordering = ('-regiao',)

admin.site.register(CidadesRegiao, CidadesRegiaoAdmin)
