from src.update._update_functions import OdooConnection
from src.manipulation._manipulation_functions import load_json_from_processed
import time
import os


# Cargar .env solo si no estamos en GitHub Actions
if os.getenv("GITHUB_ACTIONS") is None: 
    from dotenv import load_dotenv 
    load_dotenv()

# Obtener las variables de entorno
IRE_URL = os.getenv("IRE_URL")
IRE_DB = os.getenv("IRE_DB")
IRE_USERNAME = os.getenv("IRE_USERNAME")
IRE_PASSWORD = os.getenv("IRE_PASSWORD")

def main():
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
        odoo_lead['user_id'] = 9 #usuario al que se le asigna el lead (Mariana)
        # Remove None values from the dictionary
        odoo_lead = {key: value for key, value in odoo_lead.items() if value is not None}

        # Update lead in Odoo server with the new data 
        odoo.models.execute_kw(odoo.db, odoo.uid, odoo.password, 'crm.lead', 'create', [odoo_lead])
        print('Lead with ID {} created successfully'.format(lead['id']))
        time.sleep(1)
