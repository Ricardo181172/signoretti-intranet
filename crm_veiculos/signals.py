from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Veiculos

@receiver(pre_save, sender=Veiculos)
def todos_maiusculos(sender, instance, **kwargs):
    # Verifica se 'descricao' não é nulo antes de aplicar upper()
    if instance.serie:
        instance.serie = instance.serie.upper()
    if instance.chassi:
        instance.chassi = instance.chassi.upper()
