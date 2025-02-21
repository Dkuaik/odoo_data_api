# Author: <NAME>
# Date: 2025-02-21
# Description: This script is used to extract and process the EB leads in the EB system.

from datetime import datetime
from src.extraction._extraction_functions import eb_request
import json
from pathlib import Path
from datetime import datetime, timedelta, timezone
import urllib.parse
import os
from dotenv import load_dotenv

# Load the environment variables
if os.getenv("GITHUB_ACTIONS") is None:
    load_dotenv('.env')



def main():
    EB_API_KEY = os.getenv("EB_API_KEY")
    EB_EMAIL = os.getenv("EB_EMAIL")
    # Calcular los timestamps de las últimas 24 horas en formato ISO 8601 con milisegundos y UTC
    now = datetime.now(timezone.utc)
    happened_before = now.isoformat(timespec='milliseconds')
    happened_after = (now - timedelta(days=2)).isoformat(timespec='milliseconds')

    # URL parameters

    url_base = 'https://api.easybroker.com/v1/contact_requests'
    url_params = {
        'page': 1,
        'limit': 20,
        'happened_after': happened_after,
        'happened_before': happened_before
    }
    # URL creation for the EasyBroker API

    base_url = "https://api.easybroker.com/v1/contact_requests"
    eb_request_url = f"{base_url}?{urllib.parse.urlencode(url_params)}"

    # Conection with the EB API and leads extraction

    new_leads = []

    while True:
        try:
            # Obtención de datos
            eb_leads = eb_request(api_key=EB_API_KEY, url=eb_request_url)
            
            # Verificando si eb_leads no es None y tiene contenido
            if eb_leads and 'content' in eb_leads:
                new_leads.extend(eb_leads['content'])
            
            # Verificando si hay más páginas
            next_page = eb_leads.get('pagination', {}).get('next_page') if eb_leads else None
            
            if next_page:
                eb_request_url = next_page
            else:
                break
        except Exception as e:
            print(f"Error during data retrieval: {e}")
            break


    # Generation of the path to save the file

    project_dir = Path(__file__).resolve().parents[2]
    relative_path = 'data/raw/eb_leads.json'
    file_path = project_dir / relative_path

    # Saving the leads to a csv file

    with open (file_path, 'w') as file:
        json.dump(new_leads, file, indent=4)

    print(f"Datos extraídos con éxito, {len(new_leads)} leads escritos")

main()
