from django.apps import AppConfig


class CrmTiposMetaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_tipos_meta'

    def ready(self):
        import crm_tipos_meta.signals
