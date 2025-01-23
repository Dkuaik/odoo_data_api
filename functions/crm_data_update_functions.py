import time

def crm_lead_update(leads: list, updating_fields: list, credentials: tuple) -> None:
    """
    Esta función actualiza registros en la tabla 'crm.lead' de Odoo, por medio, solamente de ids.
    leads: list has to have the following format: [{'id':123, 'user_id':list , 'stage_id': list}]
    credentials: tuple should contain (db, uid, models, password)
    """
    db, uid, models, password = credentials
    begin = time.time()
    for lead in leads:
        lead_id = lead.pop('id')
        updates = [[lead_id], lead]
        print(updates)
        models.execute_kw(db, uid, password, 'crm.lead', 'write', updates)
        time.sleep(2)
    end = time.time()
    # results
    print("Data updated successfully, {} leads updated".format(len(leads)))
    print("Fields updated: ", updating_fields)
    print("Execution time: ", begin-end)