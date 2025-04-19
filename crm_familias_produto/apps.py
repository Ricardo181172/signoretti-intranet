from django.apps import AppConfig


class CrmFamiliasProdutoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_familias_produto'

    def ready(self):
        import crm_familias_produto.signals
