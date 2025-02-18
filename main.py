import subprocess
import json

def ejecutar_comando(comando):
    """
    Ejecuta un comando del sistema y captura su salida.

    Args:
    comando (list): Lista de strings que representa el comando y sus argumentos.

    Returns:
    str: La salida del comando.
    """
    try:
        resultado = subprocess.run(comando,capture_output=subprocess.PIPE, text=True)
        print(resultado.stdout)
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")
        print(f"Salida de error: {e.stderr}")
        return None

# Extraccion de datos de Odoo

ejecutar_comando(['python', 'CRM/leads_extraction.py'])

# Extraccion de datos de EB
#   Extraccion de datos Via API

ejecutar_comando (['python','eb_data_extraction_properties.py'])

#   Extraccion de datos por Scrapping

ejecutar_comando (['python','eb_scrapping.py'])

# Procesados de datos con IA (pruebas echas con deepseek-r1:8b)

ejecutar_comando(['python','odoo_data_api/test_ia.py'])

# Actualizacion de valores en Odoo 

ejecutar_comando(['python','crm_updating_data_from_eb.py'])