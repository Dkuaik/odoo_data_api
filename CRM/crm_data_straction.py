import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate


# Authentication

uid=authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Set variables
fields = ['id','expected_revenue','x_studio_comisin_compartida','description']

# Reading data (for example, from the 'project.project' table)

leads = models.execute_kw(db, uid, password, 'crm.lead', 'search_read', [[["active", "=", True]]], {'fields': fields, 'limit': 10})


# Writing data

for lead in leads:
    if lead['x_studio_comisin_compartida'] == 0:
        valor_inmueble = 0
    else:
        valor_inmueble = lead['expected_revenue'] / lead['x_studio_comisin_compartida']
    lead.update({'valor_inmueble': valor_inmueble})

with open('data/crm_leads.json', 'w') as file:
    json.dump(leads, file, indent=4)

# results
print("Data extracted successfully, {} leads written".format(len(leads)))