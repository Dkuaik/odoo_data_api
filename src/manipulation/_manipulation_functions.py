import json
from pathlib import Path
import re
from bs4 import BeautifulSoup


def load_json_from_raw(file_path: str) -> dict:

    # Generation of the path to load the file
    project_dir = Path(__file__).resolve().parents[2]
    relative_path = f'data/raw/{file_path}'
    file_path = project_dir / relative_path

    # Loading the leads from a json file
    with open(file_path, 'r') as file:
        data = json.load(file)

    if data:
        return data
    else:
        raise ValueError(f"File {file_path} is empty")

def load_json_from_processed(file_path: str) -> dict:

    # Generation of the path to load the file
    project_dir = Path(__file__).resolve().parents[2]
    relative_path = f'data/processed/{file_path}'
    file_path = project_dir / relative_path

    # Loading the leads from a json file
    with open(file_path, 'r') as file:
        data = json.load(file)

    if data:
        return data
    else:
        raise ValueError(f"File {file_path} is empty")
    
def save_json_to_raw(data: dict, file_path: str) -> None:
    
    # Generation of the path to save the file
    project_dir = Path(__file__).resolve().parents[2]
    relative_path = f'data/raw/{file_path}'
    file_path = project_dir / relative_path

    # Saving the leads to a json file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def save_json_to_processed(data: dict, file_path: str) -> None:
    
    # Generation of the path to save the file
    project_dir = Path(__file__).resolve().parents[2]
    relative_path = f'data/processed/{file_path}'
    file_path = project_dir / relative_path

    # Saving the leads to a json file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def process_leads(data_raw, data_updated):
    """
    Procesa los leads de un archivo JSON, extrae y limpia los datos necesarios, y guarda los resultados en otro archivo JSON.

    Args:
    data_raw (str): La ruta del archivo JSON con los datos sin procesar.
    data_updated (str): La ruta del archivo JSON donde se guardarán los datos actualizados.
    """
    with open(data_raw) as file:
        leads_odoo = json.load(file)

    for lead in leads_odoo:
        html_content = lead['content']
        element = find_element_by_class_and_tag(html_content, 'div', 'digits')
        if element is None:
            element = find_element_by_class_and_tag(html_content, 'span', 'listing-type-price')
        if element:
            price, currency = clean_currency(element.text)
            lead['element_found'] = element.text
            lead['x_studio_valor_del_inmueble_scrapeado'] = price
            lead['x_studio_moneda_1'] = currency
        else:
            print('Price not found')

        lead.pop('content')
        
    with open(data_updated, 'w') as file:
        json.dump(leads_odoo, file, indent=4)
        print('Data updated successfully')

    # results 
    print(f'Data extracted successfully, {len(leads_odoo)} leads updated')

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
