from CRM.credencials import url, db, username, password
from crm_data_extraction import crm_data_extraction
from crm_data_update_functions import crm_lead_update
import json

credentials = (url, db, username, password)

fields = ['id', "x_studio_comisin_compartida"]

# Llamada a la función con el argumento 'limit' para obtener todos los registros
crm_data_extraction(credentials, fields, 'data/crm_leads_comision_historia.json', limit="all")

# Actualizacion de todas las comisiones compartidas a 0

with open('data/crm_leads_comision_historia.json') as file:
    leads = json.load(file)

for lead in leads:
    lead['x_studio_comisin_compartida'] = 0

# Llamada a la función de actualización
crm_lead_update(credentials, leads)


with open('data/crm_leads_comision_historia.json') as file:
    leads = json.load(file)

# Llamada a la función de actualización
crm_lead_update(credentials, leads)
