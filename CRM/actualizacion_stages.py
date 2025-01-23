import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate

def actualizar_user_id(user_id):
    user_id_map = {
        724: 747,
        736: 9
    }
    # Si el user_id es False o no existe en el mapa, asignar 9
    if user_id is False:
        return 9
    return user_id_map.get(user_id, 9)

def actualizar_stage_id(stage_id):
    stage_id_map = {
        5: 39,
        6: 41,
        11: 41,
        8: 41,
        7: 40,
        9: 42
    }
    # Si el stage_id es False o no existe en el mapa, asignar 39
    if stage_id is False:
        return 39
    return stage_id_map.get(stage_id, 39)

# Authentication

uid=authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Set variables
fields = ['id','stage_id','user_id']

# Reading data (for example, from the 'project.project' table)

leads = models.execute_kw(db, uid, password, 'crm.lead', 'search_read', [[["active", "=", True]]], {'fields': fields})

print(leads)

with open('data/crm_stage_update.json', 'w') as file:
    json.dump(leads, file, indent=4)

# Actualizar leads
for lead in leads:
    if lead['user_id'] == False:
        lead['user_id'] = 9
    else:
        lead['user_id'] = actualizar_user_id(lead['user_id'][0])
    if lead['stage_id'] == False:
        lead['stage_id'] = 39
    else:
        lead['stage_id'] = actualizar_stage_id(lead['stage_id'][0])

# Guardar los datos actualizados en un archivo JSON
with open('data/crm_stage_update.json', 'w') as file:
    json.dump(leads, file, indent=4)

# results
print("Data extracted and updated successfully, {} leads written".format(len(leads)))