import json 
import matplotlib.pyplot as plt


with open('data/lead_crm_odoo.json') as f:
    data = json.load(f)

# Extract the 'x_studio_comisin_compartida' field
comision_compartida = [item['x_studio_comisin_compartida'] for item in data if item['x_studio_comisin_compartida'] is not None and 0.3>item['x_studio_comisin_compartida'] > 0]
print(comision_compartida)
# Plot the histogram
print('el valor mas comun es:', max(set(comision_compartida), key=comision_compartida.count))
print('longuitu de la muestra es :', len(comision_compartida))
