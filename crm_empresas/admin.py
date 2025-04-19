from django.contrib import admin
from .models import Empresas

class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'tipo_empresa', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('nome', 'cidade')
    list_filter = ('nome', 'cidade')
    ordering = ('-nome',)

admin.site.register(Empresas, EmpresasAdmin)
