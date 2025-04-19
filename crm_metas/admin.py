from django.contrib import admin
from .models import Metas

class MetasAdmin(admin.ModelAdmin):
    list_display = ('mes', 'ano', 'tipo_meta', 'produto', 'vendedor', 'quantidade', 'valor', 'status', 'data_criacao', 'data_ultima_edicao')
    search_fields = ('tipo_meta', 'produto', 'vendedor')
    list_filter = ('mes', 'ano')
    ordering = ('-tipo_meta',)

admin.site.register(Metas, MetasAdmin)
