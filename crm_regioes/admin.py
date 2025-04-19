from django.contrib import admin
from .models import Regioes

class RegioesAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('-descricao',)

admin.site.register(Regioes, RegioesAdmin)
