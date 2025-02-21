import requests
import json
from bs4 import BeautifulSoup
# from src.manipulation._manipulation_functions import find_element_by_class_and_tag
import re
import unicodedata
import time
import subprocess


begin = time.time()
baseURL = 'http://localhost:11434'

def ia_information_clean(text, format, model: str,stream=False, response_format="json"):

    print('request to url: {}/api/generate'.format(baseURL))
    ia_ollama_run_model = subprocess.run(["ollama", "run", model], capture_output=True, text=True )
    print(ia_ollama_run_model.stdout)
    # body ={
    #     "model": model,
    #     "prompt": text,
    #     "stream": stream,
    #     "format": response_format
    # }

    # response = requests.post("{}/api/generate".format(baseURL), json=body)

    # if response.status_code == 200:
    #     return response
    # else:
    #     print(response.status_code)

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


ia_information_clean('hola', 'json', 'mistral', stream=False, response_format="json")