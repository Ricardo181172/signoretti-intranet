from django.apps import AppConfig


class CrmTiposComissaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_tipos_comissao'

    def ready(self):
        import crm_tipos_comissao.signals
