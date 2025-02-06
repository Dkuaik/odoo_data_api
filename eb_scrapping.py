import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
import time
import re
import validators


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
        'US$': 'USA',  # Dolares
        '€': 'EUR',  # Euros
        '$': 'MXN',  # Pesos mexicanos
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
    
    return cleaned_value_float, currency_type

def is_valid_url(data):
    """
    Verifica si el dato proporcionado es una URL válida.

    Args:
    data: El dato que se desea verificar.

    Returns:
    bool: True si el dato es una URL válida, False en caso contrario.
    """
    if isinstance(data, str) and validators.url(data):
        return True
    return False

def find_element_by_class_and_tag(html_content, tag, class_name):
    """
    Encuentra un elemento en el contenido HTML dado su etiqueta y clase.

    Args:
    html_content (str): El contenido HTML completo.
    tag (str): La etiqueta del elemento que se desea encontrar.
    class_name (str): La clase del elemento que se desea encontrar.

    Returns:
    element: El elemento encontrado o None si no se encuentra.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    element = soup.find(tag, class_=class_name)
    return element

def fetch_url(url):
    """
    Realiza una solicitud GET a la URL proporcionada con un User-Agent específico.

    Args:
    url (str): La URL a la que se desea hacer la solicitud.

    Returns:
    response: La respuesta de la solicitud.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print('Success value {}'.format(response.status_code))
    else:
        print(f'Error: {response.status_code}')
    
    time.sleep(1)
    return response


data = 'data/lead_crm_odoo.json'

with open(data) as file:
    leads_crm_odoo = json.load(file)


for lead in leads_crm_odoo:
    if not is_valid_url(lead['x_studio_link_de_eb_url']):
        print('Invalid URL in lead {}'.format(lead['id']))
        lead['content'] = 'Null'
        continue

    url = lead['x_studio_link_de_eb_url']
    response = fetch_url(url)
    lead['content'] = str(response.content)
    count = 0

with open('data/lead_crm_odoo_updated.json', 'w') as file:
    json.dump(leads_crm_odoo, file, indent=4)
    print('Data updated successfully')
