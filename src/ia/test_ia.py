import requests
import json
from bs4 import BeautifulSoup
from src.manipulation._manipulation_functions import find_element_by_class_and_tag
import re
import unicodedata
import time

begin = time.time()
baseURL = 'http://localhost:11434'

def test_ia(text, format):
    print('request to url: {}/api/generate'.format(baseURL))

    body ={
        "model": "qwen2:7b",
        "prompt": text,
        "stream": False,
        "format": "json"
    }

    response = requests.post("{}/api/generate".format(baseURL), json=body)

    if response.status_code == 200:
        return response
    else:
        print(response.status_code)

def html_to_text(html_content):
    """
    Convierte el contenido HTML a texto plano eliminando todas las etiquetas y contenido innecesario.

    Args:
    html_content (str): El contenido HTML a convertir.

    Returns:
    str: El texto plano extraído del HTML.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator=' ', strip=True)
    return text

def extract_and_convert_to_json(text):
    """
    Extrae el contenido entre delimitadores ```json y ``` y lo convierte a JSON.

    Args:
    text (str): El texto que contiene el contenido delimitado.

    Returns:
    dict: El contenido convertido a JSON.
    """
    # Expresión regular para capturar el contenido entre ```json y ```
    json_content = text
    
    if True:
        try:
            return json.loads(json_content)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON: {e}")
            return None
    else:
        print("No se encontró contenido JSON delimitado.")
        return None

def limpiarTexto(texto):
    # 1. Elimina las secuencias literales "\r" y "\n"
    result = re.sub(r'\\[rn]', '', texto)
    
    # 2. Reemplaza múltiples espacios por uno solo.
    result = re.sub(r' {2,}', ' ', result)
    
    # 3. Normaliza el texto (forma NFD separa los acentos de las letras).
    result = unicodedata.normalize('NFD', result)
    
    # 4. Elimina los caracteres diacríticos (acento, tilde, etc.).
    result = ''.join(char for char in result if not unicodedata.combining(char))
    
    return result

estructura_output = {      
    "title": {
        "description": "Título del anuncio de la propiedad",
        "type": "string",
        "value": None
    },
    "location": {
        "description": "Ubicación de la propiedad",
        "type": "string",
        "value": None
    },
    "operations": {
        "description": "Lista de operaciones disponibles para la propiedad (venta o renta)",
        "type": "array",
        "items": 
        [
            {
            "type": "object",
            "operation": 
            {
                "type": 
                {
                    "description": "Tipo de operación (venta o renta)",
                    "type": "string",
                    "enum": ["venta", "renta"],
                    "value": None
                },
                "price": 
                {
                    "description": "Precio de la operación",
                    "type": "number",
                    "value": None
                },
                "currency": 
                {
                    "description": "Moneda de la transacción (MXN, USD, EUR)",
                    "type": "string",
                    "enum": ["MXN", "USD", "EUR"],
                    "value": None
                }
            }
            }
        ]
    },
    "agent": {
        "description": "Nombre del agente o empresa que gestiona la propiedad",
        "type": "string",
        "value": None
    }
}

with open('data/lead_crm_odoo_updated.json') as file:
    leads_crm_odoo = json.load(file)


# Limpieza de texto
ia_parser=[]
for lead in leads_crm_odoo:
    try:
        soup = BeautifulSoup(lead['content'], 'lxml')
        soup.find(tag='div', class_='listing__detail')
        result = soup.get_text()
        result = limpiarTexto(result)  # Eliminar \n y \r
    except:
        continue

    # Generación de prompt para la IA
    prompt = '''
    Extrae y organiza la información de un inmueble contenida en el 
    siguiente código HTML.
    Si no se encuentra información del inmueble en el HTML proporcionado, devuelve exactamente: None
    HTML = {}
    Respond using JSON, que sea parecido a esto {}
    '''.format(result,estructura_output)

    # print(prompt)

    response = test_ia(prompt, estructura_output)
    try:
        response = response.json()
        json_response = extract_and_convert_to_json(response['response'])
        #ids
        json_response['id'] = lead['id']
        json_response['eb_id'] = lead["x_studio_cdigo_eb"]
        ia_parser.append(json_response)
    except:
        continue
    print(response['response'])

    


    with open ('data/ia.json','w') as file:
        json.dump(ia_parser,file,indent=4)

end = time.time()

num_leads = len(ia_parser)
execution_time = end-begin
print(f"Se escribieron correctamente {num_leads} leads en {execution_time:.2f} segundos.")