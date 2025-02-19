# Proyecto de Integración y Procesamiento de Datos para Odoo CRM

Este proyecto está diseñado para gestionar, procesar y actualizar datos en un sistema Odoo CRM, utilizando técnicas de extracción, manipulación y actualización de datos, así como funcionalidades de inteligencia artificial. La estructura del proyecto es modular, facilitando el mantenimiento, la escalabilidad y la legibilidad del código.

## Estructura del Proyecto
El proyecto está organizado en carpetas y subcarpetas según su funcionalidad:

### 1. `src/` (Código Fuente)
#### `extraction/`
Contiene funcionalidades para la extracción de datos de diferentes fuentes (CRM, EB, etc.).
- **Archivos clave:** `data_extraction.py`, `eb_scrapping.py`, `crm_data_structure_extraction.py`

#### `manipulation/`
Procesa y transforma los datos para su uso en el sistema.
- **Archivo clave:** `data_manipulation.py`

#### `update/`
Gestiona la actualización de datos dentro del sistema Odoo CRM.
- **Archivos clave:** `data_update.py`, `crm_comision_updating.py`, `crm_leads_update.py`

#### `ia/`
Funcionalidades de inteligencia artificial, como la generación de información adicional para los registros.
- **Archivo clave:** `test_ia.py`

#### `utils/`
Funciones auxiliares y utilidades compartidas por el proyecto.
- **Archivos clave:** `credencials.py`, `data_validation.py`

### 2. `data/`
#### `raw/`
Almacena los datos en bruto antes de ser procesados.
- **Ejemplos:** `crm_leads.json`, `historical_properties.json`

#### `processed/`
Contiene los datos procesados y listos para su uso.
- **Ejemplo:** `lead_crm_odoo_updated.json`

### 3. `documentation/`
Incluye la documentación del proyecto.
- **Archivos clave:**
  - `crm_fields.md` - Documentación de los campos del CRM.
  - `project_available_fields.md` - Campos disponibles en el proyecto.
  - `tasks_structure.md` - Estructura de las tareas.
  - `projects_structure.json` - Estructura de los proyectos en formato JSON.

### 4. `tests/`
Contiene pruebas unitarias e integrales del proyecto.
- **Archivos clave:** `tests.py`, `tests.ipynb`

### 5. `requirements.txt`
Lista de dependencias necesarias para ejecutar el proyecto.

### 6. `main.py`
Punto de entrada principal del proyecto.

## Características Principales
✅ **Extracción de Datos**: Obtención de datos desde diversas fuentes como CRM y EB.
✅ **Manipulación de Datos**: Procesamiento y transformación para su correcto uso.
✅ **Actualización de Datos**: Modificación y actualización de registros en Odoo CRM.
✅ **Inteligencia Artificial**: Generación automática de información adicional para los registros.
✅ **Validación de Datos**: Garantiza la integridad y coherencia de la información almacenada.

## Instalación y Configuración

### 1. Instalar Dependencias
Ejecuta el siguiente comando en la terminal para instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```

### 2. Configurar Credenciales
Edita el archivo `credencials.py` con tus credenciales de acceso a Odoo.

### 3. Ejecutar Tests
Para verificar que todo funcione correctamente, ejecuta las pruebas con:
```bash
python -m pytest tests/
```

### 4. Ejecutar el Proyecto
Para iniciar el proyecto, usa el siguiente comando:
```bash
python main.py
```

## Contacto
Para más información o colaboraciones, contactar con:
📩 [Tu Nombre] - [Tu Correo Electrónico]

## Agradecimientos
Este proyecto hace uso de las siguientes bibliotecas y recursos:
- [Menciona cualquier biblioteca, framework o recurso externo utilizado]