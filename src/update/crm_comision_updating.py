from credencials import url, db, username, password, authenticate
import json
from data_update import format_for_execute_kw, update_crm_leads
import time
import xmlrpc

# Autenticación en Odoo
auth = authenticate(url, db, username, password)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# Carga de datos desde el archivo JSON
with open('data/leads_for_updating.json', 'r') as file:
    leads = json.load(file)  # Corrección: usar json.load() en lugar de file.json()

# Actualización de leads
for lead in leads:
    update_crm_leads(db,auth,password,models, lead_data=lead)  # Corrección: pasar 'auth' primero como conexión Odoo
    print('Lead con id {} escrito exitosamente'.format(lead['id']))
    time.sleep(1)
