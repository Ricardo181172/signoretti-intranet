from django.contrib import admin
from .models import Tecnico

class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('usr_cod_usuario', 'usr_nome_usuario', 'usr_login', 'usr_email', 'emp_cod_filial')
    list_filter = ('emp_cod_filial', 'emp_cidade')
    search_fields = ('usr_nome_usuario', 'usr_login', 'usr_email', 'emp_nome')

admin.site.register(Tecnico, TecnicoAdmin)
