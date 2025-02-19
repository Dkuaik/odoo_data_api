import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate
import time
from data_update import format_for_execute_kw, flatten_data
from datetime import datetime
import requests
import subprocess
# Authentication

uid = authenticate(url, db, username, password)

def obtener_campos_actualizados(odoo_leads, scrapped_leads, campo_mapeo):
    actualizaciones = []
    for odoo_lead in odoo_leads:
        lead_id = odoo_lead['id']
        scrapped_lead = next((lead for lead in scrapped_leads if lead['id'] == lead_id), None)
        if not scrapped_lead:
            print(f'Skipping lead with ID {lead_id} because it does not exist in scrapped leads')
            continue

        update_data = {key: odoo_lead.get(key, None) for key in campo_mapeo.keys()}  # Inicializar con None

        for odoo_key, scrapped_key in campo_mapeo.items():
            keys = scrapped_key.split('.')
            data = scrapped_lead
            for k in keys:
                if k in data:
                    data = data[k]
                else:
                    data = None
                    break
            if data is not None and (odoo_lead.get(odoo_key) in [None, '', 0, False]):
                update_data[odoo_key] = data
        update_data["x_studio_last_updated"] = datetime.now().isoformat()
        actualizaciones.append(update_data)

    return actualizaciones

def ia_generated_information(prompt, model):
    baseURL = 'http://localhost:11434'
    body = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post("{}/api/generate".format(baseURL), json=body)

    if response.status_code == 200:
        return response.json()  # Assuming the response is in JSON format
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Mapeo de campos
campo_mapeo = {
    "id":"id",
    "x_studio_cdigo_eb": "eb_id",
    "x_studio_api_testing": "title.value",  # No había un campo exacto, puedes ajustar
    "x_studio_inf_generada_por_ia": "location.value",  # Ajusta si hay un campo mejor
    "x_studio_valor_del_inmueble": "operations.price.value",
    # "x_studio_moneda_1": "operations[0].operation.currency.value",
    "x_studio_comisin_compartida": "operations.type.value",  # No hay un campo exacto para tipo de operación
    "x_studio_nombre_asesor_vendedor": "agent.value"
}


with open('data/ia.json') as file:
    scrapped_leads = json.load(file)

with open('data/lead_crm_odoo.json') as file:
    odoo_leads = json.load(file)

  
actualizaciones = obtener_campos_actualizados(odoo_leads,scrapped_leads,campo_mapeo)
# Imprimir el JSON de manera legible
model = 'qwen2:7b'
updates=[]
for lead in actualizaciones:     
    prompt = "Has un resumen de la propiedad para que lo lean los humanos con la siguiente informacion {}".format(lead)
    lead["x_studio_inf_generada_por_ia"] = ia_generated_information(prompt,model)['response']
    print("lead escrito {}".format(lead["id"]))
    updates.append(lead)
    with open('data/leads_for_updating.json','w') as file:
        json.dump(updates,file,indent=4)

print(json.dumps(actualizaciones[0], indent=4))