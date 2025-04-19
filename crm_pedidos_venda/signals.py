from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import PedidosVenda
from crm_veiculos.models import Veiculos  # Importe o modelo Veiculos explicitamente

@receiver(pre_save, sender=PedidosVenda)
def todos_maiusculos(sender, instance, **kwargs):
    if instance.observacoes:
        instance.observacoes = instance.observacoes.upper()
    if instance.situacao_financiamento:
        instance.situacao_financiamento = instance.situacao_financiamento.upper()

@receiver(post_save, sender=PedidosVenda)
def update_veiculo(sender, instance, created, **kwargs): 
    try:
        # Obter o veículo atualizado do banco de dados
        veiculo = instance.veiculo
        
        # Verificar se o veículo existe
        if not veiculo:
            print(f"Veículo não encontrado para o pedido {instance.id}")
            return
            
        # Registrar estado anterior para debug
        situacao_anterior = veiculo.situacao
        
        # Atualizar o valor de venda
        veiculo.valor_venda = instance.valor
        veiculo.data_venda = None
        
        # Atualizar a situação com base no status do financiamento
        if instance.status_financiamento == 'FATURADO':
            veiculo.situacao = 'FATURADO S/R'            
        elif instance.status_financiamento == 'PAGO':
            veiculo.situacao = 'VENDIDO'
            veiculo.data_venda = timezone.now().date()
        else:
            veiculo.situacao = 'EM PEDIDO'
            veiculo.data_pedido = instance.data_pedido           
        
        # Salvar as alterações no veículo
        veiculo.save(update_fields=['valor_venda', 'situacao', 'data_venda', 'data_pedido'])
        
        print(f"Veículo {veiculo.id} atualizado: situação alterada de '{situacao_anterior}' para '{veiculo.situacao}'")
    
    except Exception as e:
        print(f"Erro ao atualizar veículo: {str(e)}")