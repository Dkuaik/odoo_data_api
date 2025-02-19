def odoo_data_extraction(odoo_connection, 
                         fields = ['read'], 
                         model='res.partner', 
                         action="search_read", 
                         limit=1, 
                         active = True
                         ):
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
        model,
        action,
        [[["active", "=", active]]],
        {'fields': fields, 'limit': limit}
    )

    return leads
