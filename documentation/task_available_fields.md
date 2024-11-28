

### Información General de la Tarea
- `id`: Identificador único de la tarea (int)
- `name`: Nombre de la tarea (string)
- `description`: Descripción de la tarea (string, puede ser null)
- `create_date`: Fecha de creación de la tarea (datetime)
- `write_date`: Fecha de última modificación de la tarea (datetime)
- `project_id`: ID y nombre del proyecto al que pertenece la tarea (array: int, string)
- `state`: Estado de la tarea (string)
- `stage_id`: ID y nombre de la etapa actual de la tarea (array: int, string)

### Temporizador y Seguimiento
- `timer_start`: Indica si el temporizador de la tarea está iniciado (bool)
- `timer_pause`: Indica si el temporizador está pausado (bool)
- `is_timer_running`: Indica si el temporizador está activo (bool)
- `duration_tracking`: Tiempo acumulado de seguimiento en segundos (dict: int: int)

### Mensajes y Actividades
- `has_message`: Indica si la tarea tiene mensajes (bool)
- `message_ids`: Lista de IDs de mensajes asociados a la tarea (array de int)
- `activity_ids`: Lista de IDs de actividades asociadas a la tarea (array de int)
- `activity_state`: Estado de la actividad asociada (bool)

### Asignación y Horarios
- `date_assign`: Fecha de asignación de la tarea (datetime)
- `date_deadline`: Fecha límite de la tarea (datetime)
- `allocated_hours`: Horas asignadas a la tarea (float)
- `remaining_hours`: Horas restantes en la tarea (float)

### Progreso y Esfuerzo
- `progress`: Progreso de la tarea en porcentaje (float)
- `effective_hours`: Horas efectivas trabajadas en la tarea (float)
- `total_hours_spent`: Total de horas empleadas en la tarea (float)
- `subtask_effective_hours`: Horas efectivas trabajadas en subtareas (float)

### Usuario y Acceso
- `user_ids`: ID de los usuarios responsables de la tarea (array de int)
- `portal_user_names`: Nombre de usuario en el portal (string)
- `company_id`: ID de la compañía (int, puede ser null)
- `priority`: Nivel de prioridad de la tarea (int)
- `project_privacy_visibility`: Nivel de privacidad del proyecto (string)
- `access_url`: Enlace de acceso a la tarea en el portal (string)

### Información de Documentos
- `project_use_documents`: Indica si el proyecto utiliza documentos (bool)
- `documents_folder_id`: ID y nombre de la carpeta de documentos del proyecto (array: int, string)
- `document_count`: Número de documentos asociados a la tarea (int)
- `shared_document_count`: Número de documentos compartidos (int)

### Facturación y Horas
- `allow_billable`: Indica si la tarea es facturable (bool)
- `portal_remaining_hours`: Horas restantes para el usuario del portal (float)
- `portal_effective_hours`: Horas efectivas trabajadas visibles en el portal (float)
- `portal_total_hours_spent`: Total de horas empleadas visibles en el portal (float)

### Dependencias y Subtareas
- `subtask_count`: Número de subtareas asociadas a esta tarea (int)
- `closed_subtask_count`: Número de subtareas cerradas (int)
- `dependent_tasks_count`: Número de tareas dependientes (int)

### Otras Configuraciones
- `recurring_task`: Indica si la tarea es recurrente (bool)
- `pricing_type`: Tipo de precio de la tarea (string)
- `analytic_account_id`: ID y nombre de la cuenta analítica asociada (array: int, string)