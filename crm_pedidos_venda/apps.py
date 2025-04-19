from django.apps import AppConfig


class CrmPedidosVendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm_pedidos_venda'

    def ready(self):
        import crm_pedidos_venda.signals
