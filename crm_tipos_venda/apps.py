from django.apps import AppConfig


class CrmTiposVendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_tipos_venda'

    def ready(self):
        import crm_tipos_venda.signals
