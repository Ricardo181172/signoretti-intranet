from django.contrib import admin
from .models import Cidades

class CidadesAdmin(admin.ModelAdmin):
    list_display = ('uf', 'municipio', 'regiao', 'populacao', 'porte')
    search_fields = ('uf', 'municipio')
    list_filter = ('uf', 'municipio', 'regiao',  'populacao', 'porte')
    #date_hierarchy = 'municipio'
    ordering = ('-municipio',)

admin.site.register(Cidades, CidadesAdmin)
