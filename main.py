import subprocess
import json


with open('data/historical_properties_eb.json') as file:
    leads = json.load(file)


print('there are {} properties'.format(len(leads)))

# # Projects actualization 

# subprocess.run(['python3','project_data_extraction.py'])

# # Tasks actualizations

# subprocess.run(['python3','tasks_data_extraction.py'])

# # Reports actualizations

# subprocess.run(['python3','task_reports.py'])