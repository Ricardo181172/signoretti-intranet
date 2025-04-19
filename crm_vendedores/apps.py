from django.apps import AppConfig


class CrmVendedoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_vendedores'
    
    def ready(self):
        import crm_vendedores.signals
