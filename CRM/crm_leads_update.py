import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate
import time
from data_update import format_for_execute_kw, flatten_data

# Authentication

uid = authenticate(url, db, username, password)

# Mapeo de campos
campo_mapeo = {
    "public_id.value": "x_studio_cdigo_eb",
    "title.value": "x_studio_api_testing",  # No había un campo exacto, puedes ajustar
    "location.value": "x_studio_inf_generada_por_ia",  # Ajusta si hay un campo mejor
    "operations.price.value": "x_studio_valor_del_inmueble",
    "operations.currency.value": "x_studio_moneda_1",
    "operations.type.value": "x_studio_comisin_esperada",  # No hay un campo exacto para tipo de operación
    "agent.value": "x_studio_nombre_asesor_vendedor"
}

with open('data/ia.json') as file:
    leads = json.load(file)

with open('data/lead_crm_odoo.json') as file:
    ids_odoo = json.load(file)

flattened_leads = flatten_data(leads)
print(flattened_leads)

# Update data
# for lead in flattened_leads:
#     # ...existing code...
#     formatted_data = format_for_execute_kw(lead)
#     # ...existing code...

print("Data updated successfully, {} leads updated".format(len(flattened_leads)))