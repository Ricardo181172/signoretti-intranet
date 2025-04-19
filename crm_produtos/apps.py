from django.apps import AppConfig


class CrmTiposEquipamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_produtos'

    def ready(self):
        import crm_produtos.signals
