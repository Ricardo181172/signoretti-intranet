from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import Vendedores

@receiver(pre_save, sender=Vendedores)
def todos_maiusculos(sender, instance, **kwargs):
    # Verifica se 'descricao' não é nulo antes de aplicar upper()
    if instance.nome:
        instance.nome = instance.nome.upper()
    if instance.sobrenome:
        instance.sobrenome = instance.sobrenome.upper()
    if instance.usuario_crm:
        instance.usuario_crm = instance.usuario_crm.upper()
