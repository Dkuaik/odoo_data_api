import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate
import time

# Authentication

uid=authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

with open('data/crm_stage_update.json') as file:
    leads = json.load(file)

# Update data

updates = []
for lead in leads:
    lead_id = lead['id']
    update_data = {
        'user_id': lead['user_id'],
        'stage_id': lead['stage_id'],
    }
    updates = [[lead_id], update_data]
    print(updates)
    models.execute_kw(db, uid, password, 'crm.lead', 'write', updates)
    time.sleep(2)


print (updates)
# results
print("Data updated successfully, {} leads updated".format(len(leads)))