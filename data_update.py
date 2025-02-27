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



# Example usage:
# data = {'id': 123, 'name': 'Newer partner', 'email': 'new@example.com'}
# formatted_data = format_for_execute_kw(data)
# print(formatted_data)  # Output: ([123], {'name': 'Newer partner', 'email': 'new@example.com'})

# Example usage:
# with open('data/ia.json') as file:
#     data = json.load(file)
# flattened_data = flatten_data(data)
# print(flattened_data)
