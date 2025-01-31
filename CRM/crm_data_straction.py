import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate


# Authentication

uid=authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Set variables
fields = ['id',
        'x_studio_comisin_compartida',
        'x_studio_cdigo_eb',
        'x_studio_valor_del_inmueble',
        'x_studio_link_de_eb_url',
        ]

# Reading data (for example, from the 'project.project' table)

leads = models.execute_kw(db, uid, password, 'crm.lead', 'search_read', [[["active", "=", True]]], {'fields': fields, 'limit': 10})


with open('data/crm_leads.json', 'w') as file:
    json.dump(leads, file, indent=4)

# results
print("Data extracted successfully, {} leads written".format(len(leads)))