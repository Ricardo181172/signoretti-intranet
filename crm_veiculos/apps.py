from django.apps import AppConfig


class CrmVeiculosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_veiculos'

    def ready(self):
        import crm_veiculos.signals
