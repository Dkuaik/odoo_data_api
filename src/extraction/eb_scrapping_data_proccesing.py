import json
from eb_scrapping import find_element_by_class_and_tag, clean_currency
import requests

def process_leads(data_raw, data_updated):
    """
    Procesa los leads de un archivo JSON, extrae y limpia los datos necesarios, y guarda los resultados en otro archivo JSON.

    Args:
    data_raw (str): La ruta del archivo JSON con los datos sin procesar.
    data_updated (str): La ruta del archivo JSON donde se guardarán los datos actualizados.
    """
    with open(data_raw) as file:
        leads_odoo = json.load(file)

    for lead in leads_odoo:
        html_content = lead['content']
        element = find_element_by_class_and_tag(html_content, 'div', 'digits')
        if element is None:
            element = find_element_by_class_and_tag(html_content, 'span', 'listing-type-price')
        if element:
            price, currency = clean_currency(element.text)
            lead['element_found'] = element.text
            lead['x_studio_valor_del_inmueble_scrapeado'] = price
            lead['x_studio_moneda_1'] = currency
        else:
            print('Price not found')

        lead.pop('content')
        
    with open(data_updated, 'w') as file:
        json.dump(leads_odoo, file, indent=4)
        print('Data updated successfully')

    # results 
    print(f'Data extracted successfully, {len(leads_odoo)} leads updated')


data_raw = 'data/lead_crm_odoo_updated.json'
data_updated = 'data/lead_updated.json'