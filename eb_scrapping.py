import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
import time


def clean_currency(value):
    """
    Limpia una cadena de texto que representa una cantidad de dinero y la convierte en un float.
    
    Args:
    value (str): La cadena de texto que representa la cantidad de dinero.
    
    Returns:
    float: La cantidad de dinero como un float.
    """
    # Eliminar el símbolo de dólar y las comas
    cleaned_value = value.replace('$', '').replace(',', '')
    return float(cleaned_value)

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
        print('Success')
    else:
        print(f'Error: {response.status_code}')
    
    time.sleep(1)
    return response


data = 'data/lead_not_matching.json'

with open(data) as file:
    not_matching_leads = json.load(file)

for lead in not_matching_leads:
    if lead['x_studio_link_de_eb_url'] == False:
        print('URL not found')
        continue
    url = lead['x_studio_link_de_eb_url']
    response = fetch_url(url)
    html_content = response.content
    element = find_element_by_class_and_tag(html_content, 'div', 'price')
    if element == None:
        element = find_element_by_class_and_tag(html_content, 'span', 'listing-type-price')
    if element:
        price = clean_currency(element.text)
        lead['new price'] = price
    else:
        print('Price not found')


    break
    

with open('data/lead_not_matching_updated.json', 'w') as file:
    json.dump(not_matching_leads, file, indent=4)
    print('Data updated successfully')

# results 
print(f'Data extracted successfully, {len(not_matching_leads)} leads updated')