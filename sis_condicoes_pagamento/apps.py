from django.apps import AppConfig


class SisCondicoesPagamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sis_condicoes_pagamento'

    def ready(self):
        import sis_condicoes_pagamento.signals

