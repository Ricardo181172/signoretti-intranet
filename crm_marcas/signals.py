from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Marcas

@receiver(pre_save, sender=Marcas)
def todos_maiusculos(sender, instance, **kwargs):
    # Verifica se 'descricao' não é nulo antes de aplicar upper()
    if instance.descricao:
        instance.descricao = instance.descricao.upper()
    if instance.sigla:
        instance.sigla = instance.sigla.upper()    
            