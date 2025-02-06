import json
import crm_data_update_functions as up
from CRM.credencials import url, db, username, password, url_test, db_test

auth = (url, db, username, password)



data_eb_path = 'data/historical_properties_eb.json'
data_crm_path = 'data/lead_crm_odoo.json'



with open(data_eb_path) as file:
    leads_eb = json.load(file)

with open(data_crm_path) as file:
    leads_crm = json.load(file)

data_updating = []
lead_not_matching = []

for lead_crm in leads_crm:
    crm_lead_updating = {}
    for lead_eb in leads_eb:
        if lead_crm['x_studio_cdigo_eb'] == lead_eb['public_id']:
            crm_lead_updating = {
                'id': lead_crm['id'],
                'x_studio_valor_del_inmueble': lead_eb['operations'][0]['amount'],
                'x_studio_api_testing':lead_eb['updated_at'],
                'x_studio_cdigo_eb': lead_eb['public_id']
            }
            data_updating.append(crm_lead_updating)
    if crm_lead_updating == {}:
        lead_not_matching.append(lead_crm)

with open('data/crm_leads_eb_updating.json', 'w') as file:
    json.dump(data_updating, file, indent=4)

with open('data/lead_not_matching.json', 'w') as file:
    json.dump(lead_not_matching, file, indent=4)


# up.crm_lead_update(auth, data_updating)


#lead en eb
print("Data extracted successfully, {} leads from EB written".format(len(leads_eb)))

#lead en crm
print("Data extracted successfully, {} leads from Odoo written".format(len(leads_crm)))

#lead en crm y eb
print("Data updated successfully, {} leads written".format(len(data_updating)))

## lead en crm pero no en eb

print("Data not matching, {} leads written".format(len(lead_not_matching)))


