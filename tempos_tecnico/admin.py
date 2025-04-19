from django.contrib import admin
from .models import TemposTecnico

class TemposTecnicoAdmin(admin.ModelAdmin):
    list_display = ('emp_cod_filial', 'usr_nome_usuario', 'tmp_ano', 'tmp_mes', 'tmp_minutos_disponivel')
    search_fields = ('usr_nome_usuario', 'emp_cod_filial')
    list_filter = ('tmp_ano', 'tmp_mes', 'emp_cod_filial')

admin.site.register(TemposTecnico, TemposTecnicoAdmin)