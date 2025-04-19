from django.contrib import admin
from .models import TiposComissao

class TiposComissaoAdmin(admin.ModelAdmin):
    list_display = ('descricao','status',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('-descricao',)

admin.site.register(TiposComissao, TiposComissaoAdmin)   
