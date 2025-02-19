import json
import xmlrpc.client
from credencials import url, db, username, password, authenticate

# Authentication

uid=authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Set variables
fields = ['name','display_name','user_id', 'alias_status']

# Reading data (for example, from the 'project.project' table)

projects = models.execute_kw(db, uid, password, 'project.project', 'search_read', [[]], {'fields': fields})

projects_list = []
for project in projects: #quitar los proyectos internos, desconozco motivo de existencia
    if project['display_name']!="Interno":
        projects_list.append(project)   

# Writing data

with open('data/projects.json', 'w') as file:
    json.dump(projects_list, file, indent=4)

# results
print("Data extracted successfully, {} projects written".format(len(projects_list)))