import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate
import time

# Authentication

uid=authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

with open('data/leads_updated.json') as file:
    leads = json.load(file)

# Update data

updates = []
for lead in leads:
    lead_id = lead['id']

    # Verificar si las claves existen en el diccionario y no son nulas o no válidas
    if ('x_studio_valor_del_inmueble_scrapeado' not in lead or 
        'x_studio_moneda_1' not in lead or 
        lead['x_studio_valor_del_inmueble_scrapeado'] is None or 
        lead['x_studio_moneda_1'] is None or 
        lead['x_studio_valor_del_inmueble_scrapeado'] == 0.0):
        print(f'Skipping lead {lead_id} due to missing or invalid keys')
        continue

    update_data = {
        'x_studio_valor_del_inmueble_scrapeado': lead['x_studio_valor_del_inmueble_scrapeado'],
        'x_studio_moneda_1': lead['x_studio_moneda_1'],
    }
    updates = [[lead_id], update_data]
    print(updates)
    models.execute_kw(db, uid, password, 'crm.lead', 'write', updates)
    time.sleep(2)


print (updates)
# results
print("Data updated successfully, {} leads updated".format(len(leads)))