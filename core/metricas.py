from django.utils.formats import number_format
from crm_veiculos.models import Veiculos
from crm_pedidos_venda.models import PedidosVenda

def get_metricas_veiculos():
     veiculos = Veiculos.objects.all()
     quantidade_veiculos = veiculos.count()
     custo_estoque = sum(veiculo.valor_custo for veiculo in veiculos)
     valor_venda = sum(veiculo.valor_venda for veiculo in veiculos)
     lucro = valor_venda - custo_estoque
     
     return dict(
          quantidade_veiculos=quantidade_veiculos,
          custo_estoque=number_format(custo_estoque, decimal_pos=2, force_grouping=True),
          valor_venda= number_format(valor_venda, decimal_pos=2, force_grouping=True),
          lucro=number_format(lucro, decimal_pos=2, force_grouping=True),          
     )

def get_metricas_pedidos_venda():
     pedidos_venda = PedidosVenda.objects.all()
     quantidade_pedidos = pedidos_venda.count()
     valor_pedidos = sum(pedido_venda.valor for pedido_venda in pedidos_venda)
     custo_pedidos = sum(pedido_venda.veiculo.valor_custo for pedido_venda in pedidos_venda)
     ticket_medio = valor_pedidos / quantidade_pedidos
     
     return dict(
          quantidade_pedidos=quantidade_pedidos,
          valor_pedidos=number_format(valor_pedidos, decimal_pos=2, force_grouping=True),
          custo_pedidos= number_format(custo_pedidos, decimal_pos=2, force_grouping=True),
          ticket_medio=number_format(ticket_medio, decimal_pos=2, force_grouping=True),          
     )
