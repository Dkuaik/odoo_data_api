import json
import xmlrpc.client

def crm_data_extraction(odoo_connection, fields, output_file, limit=10):
    """
    Extrae datos de leads de Odoo y los guarda en un archivo JSON.

    Args:
        odoo_connection (OdooConnection): Instancia de la clase OdooConnection para la conexión.
        fields (list): Lista de campos a extraer.
        output_file (str): Ruta del archivo JSON donde se guardarán los datos.
        limit (int/str): Límite de registros a extraer. Usa "all" para extraer todos los registros.
    """
    # Configuración del límite
    if limit == "all":
        limit = 0  # No limit

    # Lectura de datos usando el proxy de modelos
    leads = odoo_connection.models.execute_kw(
        odoo_connection.db,
        odoo_connection.uid,
        odoo_connection.password,
        'crm.lead',
        'search_read',
        [[["active", "=", True]]],
        {'fields': fields, 'limit': limit}
    )

    # Escritura de los datos en el archivo JSON
    with open(output_file, 'w') as file:
        json.dump(leads, file, indent=4)

    # Mensaje de confirmación
    print(f"Datos extraídos con éxito, {len(leads)} leads escritos")

