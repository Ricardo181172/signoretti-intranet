from django.contrib import admin
from .models import Ocorrencia

class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('ose_id_ocorrencia', 'os_nr_os', 'usr_nome_usuario', 'ose_dth_ocorrencia', 'ose_dsc_ocorrencia', 'trf_status')
    search_fields = ('os_nr_os', 'usr_nome_usuario', 'ose_dsc_ocorrencia', 'trf_cod_integracao', 'trf_dsc_tarefa')
    list_filter = ('ose_dth_ocorrencia', 'emp_cod_filial', 'trf_status')
    date_hierarchy = 'ose_dth_ocorrencia'
    ordering = ('-ose_dth_ocorrencia',)

admin.site.register(Ocorrencia, OcorrenciaAdmin)
