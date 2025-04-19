from django.apps import AppConfig


class CrmModelosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_modelos'

    def ready(self):
        import crm_modelos.signals
