import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate


# Authentication

uid=authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Set variables
fields = ['name','display_name','user_id', 'alias_status']

# Reading data (for example, from the 'project.project' table)

fields_info = models.execute_kw(db, uid, password, 'crm.lead', 'fields_get', [], {'attributes': ['string', 'help', 'type']})

# Writing data

with open('documentation/crm_fields_info.json', 'w') as file:
    json.dump(fields_info, file, indent=4)

# results
print("Data extracted successfully, {} fields info written".format(len(fields_info)))