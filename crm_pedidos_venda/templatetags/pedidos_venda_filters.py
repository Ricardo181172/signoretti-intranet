from django import template

register = template.Library()

@register.filter
def format_currency(value):
    try:
        # Converte o valor para float
        numeric_value = float(value)
        # Formata o número com separadores de milhar e vírgula como separador decimal
        formatted_value = f"{numeric_value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        return formatted_value
    except (ValueError, TypeError):
        return "Valor inválido"