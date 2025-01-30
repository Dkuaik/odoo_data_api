import re
import json
import unicodedata
from bs4 import BeautifulSoup
from collections import defaultdict

def html_to_json(html_string: str) -> dict:
    """
    - Recibe HTML en una cadena.
    - Convierte a texto puro.
    - Busca los campos definidos en fields_map (por su 'nombre original').
    - Asigna el valor (lo que esté tras los ":") a la clave definida en fields_map (nombre corto).
    - Ignora segundas apariciones de algunos campos, y omite el campo "Link del acuerdo entre asesores".
    - Devuelve un diccionario con toda la información extraída.
    """

    # 1. Mapeo de nombres originales (como aparece en el HTML) a nombres cortos
    fields_map = {
        "Nombre del Lead":                 "Nombre",
        "Link de EB":                      "LinkEB",
        "Link de IRE":                     "LinkIRE",
        "ID del anuncio":                  "IDAnuncio",
        "Origen y Medio de Promoción":     "OrigenProm",
        "Link de WA":                      "LinkWA",       # tomaremos la primera aparición
        "Tipo de Cliente":                 "TipoCliente",
        "Correo Electrónico":              "Correo",       # tomaremos la primera aparición
        "Asesor comprador":                "AsesorComprador",
        "Presupuesto":                     "Presupuesto",
        "Tiene aval y/o obligado solidario": "AvalObligado",
        "Método de pago":                  "MetodoPago",
        "Nombre del asesor":               "NombreAsesor",
        "Link de página web":              "LinkWeb",
        # "Link del acuerdo entre asesores": (IGNORAR, no lo incluimos en el map)
        "Comisión que comparte en porcentaje y cifra en MXN": "ComisionMXN",
        "Formato o forma que necesita para registrar al cliente": "FormatoRegistro",
        "Porcentaje de comisión":          "PorcComision",
        "Comisión compartida":             "ComisionCompartida",
        "Ingreso esperado":                "IngresoEsperado"
    }

    # 2. Set o lista de campos que NO queremos extraer en absoluto
    #    (ej. "Link del acuerdo entre asesores")
    ignore_fields = {
        "Link del acuerdo entre asesores"
    }

    # 3. Algunos campos de los cuales queremos solo la primera aparición:
    only_first_occurrence = {
        "Link de WA",
        "Correo Electrónico"
    }

    # 4. Convertir HTML a texto
    soup = BeautifulSoup(html_string, "html.parser")
    raw_text = soup.get_text(separator="\n")

    # 5. Separamos en líneas y las limpiamos
    lines = [line.strip() for line in raw_text.split("\n") if line.strip()]

    # 6. Diccionario resultado (inicialmente vacío)
    result = {}
    
    # 7. Contar apariciones para saltar duplicados en only_first_occurrence
    found_count = defaultdict(int)

    for line in lines:
        # Buscamos si en esta línea aparece alguno de los campos originales,
        # con la estructura "Campo: valor".
        for original_field, short_field in fields_map.items():
            # Si el original_field está en la lista de ignorados, skip
            if original_field in ignore_fields:
                continue

            # Verificamos si la línea empieza con "campo:" o "campo "...
            # En muchos HTML se ve "Campo: Valor", 
            # pero a veces "Campo:" podría tener espacios, etc.
            # Usaremos un split con máximo 1 partición.
            if original_field in line:
                # Intentamos separar en 2 (antes de ":" y después de ":")
                parts = line.split(":", 1)
                
                # parts[0] = lo que está antes de :, parts[1] = después de :
                if len(parts) == 2:
                    # Revisamos si lo que está antes coincide (o contiene) el original_field
                    left_side = parts[0].strip()
                    
                    # Si 'left_side' contiene el 'original_field', tomamos 'right_side'
                    if original_field in left_side:
                        right_side = parts[1].strip()
                        
                        # Checamos si ya tenemos demasiadas apariciones para este campo
                        if original_field in only_first_occurrence:
                            if found_count[original_field] > 0:
                                # Ya se encontró una vez, ignoramos la segunda
                                continue
                        
                        # Guardamos en el diccionario con el nombre corto
                        result[short_field] = right_side
                        found_count[original_field] += 1

    return result

def limpiar_texto_sin_acentos(texto):
    """
    Toma un texto de entrada:
      - Elimina acentos y signos diacríticos.
      - Elimina espacios innecesarios (leading/trailing y duplicados en medio).
    Devuelve la versión 'normalizada' sin acentos y con espacios mínimos.
    """
    # 1. Eliminar acentos y diacríticos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_acentos = ''.join(
        char for char in texto_normalizado 
        if unicodedata.category(char) != 'Mn'
    )
    
    # 2. Procesar cada línea para limpiar espacios
    lineas = texto_sin_acentos.splitlines()
    lineas_limpias = []
    
    for linea in lineas:
        # Quitar espacios al inicio y al final
        linea = linea.strip()
        # Reemplazar múltiples espacios por uno solo en el interior
        linea = re.sub(r'\s+', ' ', linea)
        lineas_limpias.append(linea)
    
    # Opcional: si se quiere eliminar por completo las líneas vacías
    # lineas_limpias = [l for l in lineas_limpias if l]

    # Reconstruir el texto con saltos de línea
    texto_final = "\n".join(lineas_limpias)
    
    return texto_final

# Cargar el archivo JSON de crm_leads.json
ruta_crm_leads = "C:/Users/rif-l/OneDrive/Escritorio/Proyectos/odoo_data_api/data/crm_leads.json"
with open(ruta_crm_leads, "r", encoding="utf-8") as archivo:
    crm_leads = json.load(archivo)

#cargar información de la descripción
texto = crm_leads[4]["description"]

resultado = html_to_json(texto)

# Guardar en un archivo JSON
ruta_archivo = "C:/Users/rif-l/OneDrive/Escritorio/Proyectos/odoo_data_api/descripciones.json"
with open(ruta_archivo, "w") as archivo:
    json.dump(resultado, archivo, ensure_ascii=False, indent=4)