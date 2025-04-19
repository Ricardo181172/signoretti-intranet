from django.contrib import admin
from .models import Agenda

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('emp_cod_filial', 'os_nr_os', 'cli_nome', 'usr_nome_usuario', 'age_dth_previsao_inicio', 'age_fstatus',)
    search_fields = ('cli_nome', 'usr_nome_usuario', 'os_nr_os', 'cli_cnpj_cpf',)
    list_filter = ('age_dth_previsao_inicio', 'age_fstatus', 'emp_cod_filial',)
    date_hierarchy = 'age_dth_previsao_inicio'
    ordering = ('-age_dth_previsao_inicio',)

admin.site.register(Agenda, AgendaAdmin)
