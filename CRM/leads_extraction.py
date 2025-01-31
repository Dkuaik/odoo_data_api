import crm_data_extraction as de
from credencials import url, db, username, password 

auth = (url, db, username, password)

fields = ['id',
        'x_studio_comisin_compartida',
        'x_studio_cdigo_eb',
        'x_studio_valor_del_inmueble',
        'x_studio_link_de_eb_url',
        ]

de.crm_data_extraction(auth,fields, 'data/lead_crm_odoo.json', limit="all")

