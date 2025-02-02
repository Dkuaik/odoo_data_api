import validators
import re

def clean_currency(value):
    """
    Limpia una cadena de texto que representa una cantidad de dinero y la convierte en un float.
    También identifica y devuelve el tipo de moneda.

    Args:
    value (str): La cadena de texto que representa la cantidad de dinero.

    Returns:
    tuple: Una tupla que contiene el tipo de moneda y la cantidad de dinero como un float.
    """
    # Identificar el tipo de moneda
    currency_symbols = {
        '$': 'USD',  # Dólares
        '€': 'EUR',  # Euros
        'MX$': 'MXN'  # Pesos Mexicanos
    }
    
    currency_type = None
    for symbol, currency in currency_symbols.items():
        if symbol in value:
            currency_type = currency
            break
    
    # Eliminar todos los caracteres que no son dígitos o puntos decimales
    cleaned_value = re.sub(r'[^\d.]', '', value)
    
    # Considerar solo el último punto decimal (el más a la derecha)
    if '.' in cleaned_value:
        last_dot_index = cleaned_value.rfind('.')
        integer_part = cleaned_value[:last_dot_index]
        decimal_part = cleaned_value[last_dot_index + 1:]
        
        if len(decimal_part) == 2:
            cleaned_value = integer_part  # Eliminar la parte decimal si tiene exactamente dos dígitos
        else:
            cleaned_value = integer_part + decimal_part  # Concatenar la parte entera y decimal si no tiene exactamente dos dígitos
    
    # Eliminar cualquier punto decimal restante
    cleaned_value = re.sub(r'\.', '', cleaned_value)
    
    try:
        cleaned_value_float = float(cleaned_value)
    except ValueError:
        print(f'Hubo un problema con la conversión de "{cleaned_value}" a float.')
        cleaned_value_float = 0.0
    
    return currency_type, cleaned_value_float

print(clean_currency('MX$ 1.000.800.00'))
