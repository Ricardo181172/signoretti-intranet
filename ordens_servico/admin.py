from django.contrib import admin
from .models import OrdemServico

class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('emp_cod_filial', 'os_nr_os', 'cli_nome', 'os_id_situacao_os', 'os_dth_abertura', 'os_fstatus')
    search_fields = ('os_nr_os', 'emp_nome', 'cli_nome', 'sit_dsc_situacao_os')
    list_filter = ('os_dth_abertura', 'os_fstatus', 'emp_uf', 'sit_cod_situacao_os')
    date_hierarchy = 'os_dth_abertura'
    ordering = ('-os_dth_abertura',)

admin.site.register(OrdemServico, OrdemServicoAdmin)
