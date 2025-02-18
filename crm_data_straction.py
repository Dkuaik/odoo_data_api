import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate


import xmlrpc.client
import json

def crm_data_extraction(auth, fields, output_file, limit=10):
    """
    Extrae datos de leads de Odoo y los guarda en un archivo JSON.

    Args:
    auth (tuple): Una tupla con la URL, base de datos, nombre de usuario y contraseña.
    fields (list): Lista de campos a extraer.
    output_file (str): Ruta del archivo JSON donde se guardarán los datos.
    limit (int/str): Límite de registros a extraer. Usa "all" para extraer todos los registros.
    """
    url, db, username, password = auth

    # Authentication
    uid = authenticate(url, db, username, password)

    # Connection to the object
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    # Reading data
    if limit == "all":
        limit = 0  # No limit
    leads = models.execute_kw(db, uid, password, 'crm.lead', 'search_read', [[["active", "=", True]]], {'fields': fields, 'limit': limit})

    with open(output_file, 'w') as file:
        json.dump(leads, file, indent=4)

    # results
    print("Data extracted successfully, {} leads written".format(len(leads)))
