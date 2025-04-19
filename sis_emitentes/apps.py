from django.apps import AppConfig


class CrmEmitentesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sis_emitentes'

    def ready(self):
        import sis_emitentes.signals  # Assumindo que seu arquivo signals está em `sis_emitentes/signals.py`
