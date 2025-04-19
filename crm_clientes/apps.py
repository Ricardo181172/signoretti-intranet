from django.apps import AppConfig


class CrmClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_clientes'

    def ready(self):
        import crm_clientes.signals
