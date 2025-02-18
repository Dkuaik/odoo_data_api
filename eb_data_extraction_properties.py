from keys import api_key
import requests
import json
import time

def get_all_properties(api_key, URL_api) -> dict:
    url = URL_api

    headers = {
        'X-Authorization': api_key,
        'accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        # print(f"Response content: {response.content}")
        return None
    elif response.status_code == 200:
        print(f"Success: {response.status_code}")
    time.sleep(1)

    return response.json()

historical_properties = []
URL = 'https://api.easybroker.com/v1/properties?page=1&limit=40'

condition=True

while condition:
    propiedades = get_all_properties(api_key,URL)
    URL = propiedades['pagination']['next_page']
    for propiedad in propiedades['content']:
        historical_properties.append(propiedad)

    if propiedades['pagination']['next_page'] == None:
        condition = False

with open('data/historical_properties.json', 'w') as file:
    json.dump(historical_properties, file, indent=4)
    print("Properties saved in historical_properties.json")
print('Success')
print(f"Total properties written: {len(historical_properties)}")