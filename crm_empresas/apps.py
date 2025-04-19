from django.apps import AppConfig


class CrmEmpresasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_empresas'

    def ready(self):
        import crm_empresas.signals
