from django.contrib import admin
from .models import Emitentes


class EmitentesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'cidade', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('codigo', 'nome')
    list_filter = ('codigo', 'nome', 'cidade')
    ordering = ('-nome',)

admin.site.register(Emitentes, EmitentesAdmin)
