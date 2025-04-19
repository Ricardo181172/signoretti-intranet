from django.contrib import admin
from .models import Vendedores

class VendedoresAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'emitente', 'e_mail', 'celular', 'usuario_crm', 'senha_crm', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('nome', 'emitente')
    list_filter = ('nome', 'sobrenome', 'emitente', 'e_mail', 'celular', 'usuario_crm', 'senha_crm', 'data_criacao', 'data_ultima_edicao')
    ordering = ('-nome',)

admin.site.register(Vendedores, VendedoresAdmin)
