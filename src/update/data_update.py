


def format_for_execute_kw(data_dict):
    """
    Formats a dictionary into the format accepted by the models.execute_kw function.
    
    Args:
        data_dict (dict): The dictionary to format. Should contain 'id' and other key-value pairs.
        
    Returns:
        tuple: A tuple in the format (id, {key: value, ...})
    """
    if 'id' not in data_dict:
        raise ValueError("The dictionary must contain an 'id' key.")
    
    id_value = data_dict.pop('id')
    return ([id_value], data_dict)

def flatten_data(data):
    """
    Flattens the information from a list of nested dictionaries into a list of key-value pair dictionaries.
    
    Args:
        data (list): The list of nested dictionaries to flatten.
        
    Returns:
        list: A list of flattened dictionaries with key-value pairs.
    """
    def _flatten(obj, parent_key='', flattened=None):
        if flattened is None:
            flattened = {}
        if isinstance(obj, dict):
            for k, v in obj.items():
                new_key = f"{parent_key}.{k}" if parent_key else k
                _flatten(v, new_key, flattened)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                new_key = f"{parent_key}.{i}" if parent_key else str(i)
                _flatten(item, new_key, flattened)
        else:
            flattened[parent_key] = obj
        return flattened
    
    return [_flatten(item) for item in data]

def update_crm_leads(db,uid,password,models, lead_data):
    """
    Actualiza un único lead del CRM en Odoo usando execute_kw
    
    Args:
        odoo_connection: Conexión activa a Odoo (objeto)
        lead_data: Diccionario con los datos a actualizar
    
    Returns:
        dict: Resultado de la actualización con éxito o error
    """
    
    try:
        
        # Verificamos que el lead tenga ID
        if not lead_data.get('id'):
            raise ValueError(f"Lead sin ID: {lead_data}")
        
        # Preparamos los datos a actualizar (excluyendo el ID)
        update_values = {k: v for k, v in lead_data.items() if k != 'id'}
        
        # Ejecutamos la actualización usando execute_kw
        result = models.execute_kw(
            db,
            uid,
            password,
            'crm.lead',  # Modelo de CRM leads
            'write',     # Método de escritura
            [[lead_data['id']], update_values]  # ID y valores a actualizar
        )
        
        if result:
            return {'status': 'success', 'message': f'Lead ID {lead_data["id"]} actualizado correctamente'}
        else:
            return {'status': 'error', 'message': f'Error al actualizar lead ID {lead_data["id"]}'}
        
    except Exception as e:
        return {'status': 'error', 'message': f'Error en lead ID {lead_data.get("id", "Unknown")}: {str(e)}'}






# Example usage:
# data = {'id': 123, 'name': 'Newer partner', 'email': 'new@example.com'}
# formatted_data = format_for_execute_kw(data)
# print(formatted_data)  # Output: ([123], {'name': 'Newer partner', 'email': 'new@example.com'})

# Example usage:
# with open('data/ia.json') as file:
#     data = json.load(file)
# flattened_data = flatten_data(data)
# print(flattened_data)
