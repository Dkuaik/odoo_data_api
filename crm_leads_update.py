import json
import xmlrpc.client
from credentials import url, db, username, password, authenticate
import time


# Authentication

uid=authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

with open('data/crm_leads.json') as file:
    leads = json.load(file)

# Update data

updates = []
for lead in leads:
    updates=[[lead['id']],{'x_studio_valor_del_inmueble': lead['valor_inmueble'], 'x_studio_api_testing': 'Updated'}]	
    models.execute_kw(db, uid, password, 'crm.lead', 'write', updates)
    time.sleep(2)
    updates.clear()


print (updates)
# results
print("Data updated successfully, {} leads updated".format(len(leads)))