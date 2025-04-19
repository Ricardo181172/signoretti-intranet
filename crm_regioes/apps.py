from django.apps import AppConfig


class CrmRegioesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_regioes'

    def ready(self):
        import crm_regioes.signals
