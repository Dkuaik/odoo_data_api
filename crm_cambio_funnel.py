import json
import xmlrpc.client
from credentials import url, db, username, password, authenticate
import time

def update_stage_id(lead):
    if lead['stage_id'][0] == 5:
        return 39
    elif lead['stage_id'][0] in [11, 8]:
        return 41
    elif lead['stage_id'][0] == 7:
        return 40
    elif lead['stage_id'][0] == 9:
        return 42
    return None

# Authentication

uid=authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# getting data

with open('data/crm_leads.json') as file:
    leads = json.load(file)

# Update stage_id




for lead in leads:
    if lead['stage_id'][0] in [5, 11, 8, 7, 9]:
        new_stage_id = update_stage_id(lead)
        update=[[lead['id']],{'stage_id':new_stage_id}] 
        models.execute_kw(db, uid, password, 'crm.lead', 'write', update)
    else:
        print('Lead {} not updated'.format(lead['id']))
    update.clear()
    time.sleep(2)

# results
print("Data updated successfully, {} leads updated".format(len(leads)))