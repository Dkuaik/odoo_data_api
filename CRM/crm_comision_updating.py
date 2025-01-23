from credencials import url_test, db_test, username, password, authenticate
from functions.crm_data_extraction_funtions import crm_data_extraction, print_hello

credentials = (url_test, db_test, username, password)

fields = ['id', "x_studio_comisin_compartida"]

# Llamada a la función con el argumento 'limit' para obtener todos los registros
crm_data_extraction(credentials, fields, 'data/crm_leads_comision_historia.json')

