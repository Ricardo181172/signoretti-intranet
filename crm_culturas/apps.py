from django.apps import AppConfig


class CrmCulturasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_culturas'

    def ready(self):
        import crm_culturas.signals

