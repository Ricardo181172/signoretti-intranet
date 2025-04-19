from django.apps import AppConfig


class CrmAcessoriosVeiculoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_acessorios_veiculo'

    def ready(self):
        import crm_acessorios_veiculo.signals

