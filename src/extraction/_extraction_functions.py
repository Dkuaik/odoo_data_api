from credencials import EB_API_KEY
import requests
import time


def odoo_data_extraction(odoo_connection, 
                         fields = ['read'], 
                         model='res.partner', 
                         action="search_read", 
                         limit=1, 
                         active = True
                         ):
    """
    Extrae datos de leads de Odoo y los guarda en un archivo JSON.

    Args:
        odoo_connection (OdooConnection): Instancia de la clase OdooConnection para la conexión.
        fields (list): Lista de campos a extraer.
        output_file (str): Ruta del archivo JSON donde se guardarán los datos.
        limit (int/str): Límite de registros a extraer. Usa "all" para extraer todos los registros.
    """
    # Configuración del límite
    if limit == "all":
        limit = 0  # No limit

    # Lectura de datos usando el proxy de modelos
    leads = odoo_connection.models.execute_kw(
        odoo_connection.db,
        odoo_connection.uid,
        odoo_connection.password,
        model,
        action,
        [[["active", "=", active]]],
        {'fields': fields, 'limit': limit}
    )

    return leads


def eb_request(api_key=EB_API_KEY,url='https://api.easybroker.com/v1/contact_requests?page=1&limit=1')-> dict:

    """
    Realiza una petición a la API de EasyBroker y devuelve la respuesta en formato JSON.
    params:
    api_key (str): Clave de la API de EasyBroker.
    url (str): URL de la API de EasyBroker.
    returns: dict
    """

    headers = {
        'X-Authorization': api_key,
        'accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
        
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None
    elif response.status_code == 200:
        print(f"Success: {response.status_code}")

    time.sleep(1)

    return response.json()