from django.apps import AppConfig


class CrmMarcasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_marcas'

    def ready(self):
        import crm_marcas.signals
