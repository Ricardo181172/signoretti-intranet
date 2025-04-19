from django.contrib import admin
from .models import AtendimentoOS

class AtendimentoOSAdmin(admin.ModelAdmin):
    list_display = ('os_nr_os', 'cli_nome', 'emp_cod_filial', 'atd_dsc_causa', 'atd_ano', 'atd_mes')
    search_fields = ('os_nr_os', 'cli_nome', 'emp_nome', 'usr_nome_usuario')
    list_filter = ('atd_ano', 'atd_mes', 'emp_uf', 'os_fstatus')
    date_hierarchy = 'atd_dth_registro'
    ordering = ('-atd_dth_registro',)

admin.site.register(AtendimentoOS, AtendimentoOSAdmin)

