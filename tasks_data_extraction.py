# this script is used to extract data from the tasks module in odoo per project. The script should be able to extract the following data:
# name, description, deadline, priority, status, assigned to, created by, creation date, last update date


import json
import xmlrpc.client
from credentials import url, db, username, password, authenticate

# Authentication

uid = authenticate(url, db, username, password)

# Connection to the object

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Set variables

fields = [
          'id', 
          'name',
        #   'state' problema con autoreferencia
          'user_ids',
          'portal_user_names', 
          'project_id', 
          'create_date', 
          'write_date', 
          'date_assign', 
          'date_deadline',
          'allocated_hours',
          'remaining_hours',
          'progress', 
          'effective_hours', 
          'total_hours_spent', 
          'subtask_effective_hours' 
        ]

tasks = []

# Reading data 

tasks_temp = models.execute_kw(db, uid, password, 'project.task', 'search_read', [[["state", "in", ["01_in_progress", "02_changes_requested", "03_approved", "04_waiting_normal"]]]], {'fields': fields})

# Filtering data without project_id
for task in tasks_temp:
    if task['project_id'] != False:
        tasks.append(task)

# Writing data

with open("data/tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

# results
print("Data extracted successfully, {} tasks written".format(len(tasks)))