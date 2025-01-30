import json
import xmlrpc.client
from credencials import authenticate

def crm_data_extraction(credentials: tuple, fields: list, file_name: str, limit: int = 10) -> None:
    """
    Esta función extrae datos de la tabla 'crm.lead' de Odoo y los guarda en un archivo JSON de nombre 'file_name'.
    credentials: tuple should contain (url, db, username, password)
    fields: list of fields to extract
    file_name: name of the file to save the extracted data
    limit: optional limit on the number of records to extract (default is 10, "all" means no limit)
    """
    url, db, username, password = credentials
    # Authentication
    uid = authenticate(url, db, username, password)
    # Connection to the object
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # Reading data
    params = {'fields': fields}
    if limit != "all":
        params['limit'] = limit
    leads = models.execute_kw(db, uid, password, 'crm.lead', 'search_read', [[["active", "=", True]]], params)
    # Writing data
    with open(file_name, 'w') as file:
        json.dump(leads, file, indent=4)
    # Results
    print("Data extracted successfully, {} leads written".format(len(leads)))

def print_hello():
    print("Hello from crm_data_extraction_functions.py")
