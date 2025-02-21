from src.manipulation._manipulation_functions import *

def main():
    # Load the data
    eb_leads = load_json_from_raw('eb_leads.json')

    # Map the fields

    field_mapping = {
        # EB_field: Odoo_field
        "id": "id",
        "name": "name",
        "phone": "phone",
        "email": "email_from",
        "property_id": "x_studio_cdigo_eb",
        "description": "description",
        "happened_at": "x_studio_happened_at",
        "contact_id": "contact_id",
        "source": "source",
        "message": "message",
        "title": "title",
    }

    # Lead title generation
    for lead in eb_leads:
        lead['title'] = lead['name'] + ' - ' + lead['phone']

    # Lead description generation
    for lead in eb_leads:
        lead['description'] = f"Source: {lead['source']}\nMessage: {lead['message']}"

    # Leads update (field renaming based on mapping)
    for lead in eb_leads:
        updated_lead = {}
        for eb_field, odoo_field in field_mapping.items():
            if eb_field in lead:
                updated_lead[odoo_field] = lead[eb_field]
        
        # Add the updated lead to the list (with title and description)
        lead.update(updated_lead)

    # Save the updated leads
    save_json_to_processed(eb_leads, 'odoo_leads_daily.json')
    print("Leads updated successfully, {} leads updated".format(len(eb_leads)))