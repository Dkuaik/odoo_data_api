from src.update._update_functions import OdooConnection
from credencials import IRE_URL, IRE_DB, IRE_USERNAME, IRE_PASSWORD
from src.manipulation._manipulation_functions import load_json_from_processed
import time

# Authentication init for Odoo server
odoo = OdooConnection(
    url=IRE_URL,
    db=IRE_DB,
    username=IRE_USERNAME,
    password=IRE_PASSWORD
)

# update data

leads = load_json_from_processed('odoo_leads_daily.json')

# read data
for lead in leads:
    odoo_lead = {key: lead[key] for key in ['name', 
                                            'phone',
                                            'email_from',
                                            'description',
                                            'x_studio_cdigo_eb',
                                            'x_studio_happened_at',
                                            ]}
    odoo_lead['name'] = lead['title']
    odoo_lead['user_id'] = 9
    # Remove None values from the dictionary
    odoo_lead = {key: value for key, value in odoo_lead.items() if value is not None}

    # Update lead in Odoo server with the new data 
    odoo.models.execute_kw(odoo.db, odoo.uid, odoo.password, 'crm.lead', 'create', [odoo_lead])
    print('Lead with ID {} created successfully'.format(lead['id']))
    time.sleep(1)
