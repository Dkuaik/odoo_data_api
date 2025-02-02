import json
from collections import defaultdict

# Standarize the strings for the project names
import re

def standardize_string(s):
    # Convertir a minúsculas
    s = s.lower()
    # Reemplazar espacios en blanco por guiones bajos
    s = s.replace(' ', '_')
    # Reemplazar caracteres no permitidos (como /) por guiones bajos
    s = re.sub(r'[\/-]', '_', s)
    # Eliminar cualquier otro carácter no alfanumérico
    s = re.sub(r'[^a-z0-9_]', '', s)
    # Reemplazar múltiples guiones bajos consecutivos por uno solo
    s = re.sub(r'_+', '_', s)
    return s


# Load the data

with open("data/tasks.json", "r") as file:
    tasks = json.load(file)

with open("data/projects.json", "r" ) as file:
    projects = json.load(file)

reports = []
task_by_project = defaultdict(list)

for task in tasks:
    if task['project_id'] == False:
        continue
    project_id = task['project_id'][0]
    task_by_project[project_id].append(task)

for project in projects:
    project_id = project['id']
    project_name = standardize_string(project['name'])
    
    with open(f"reports/{project_name}.json", "w") as file:
        json.dump(task_by_project[project_id], file, indent=4)
