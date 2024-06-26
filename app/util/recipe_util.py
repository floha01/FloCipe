import json

import requests


def search_recipe(query):
    api_id = '9422b38e'
    api_key = '22d0363e0ff655a4cc2b14a5c9901e24'
    endpoint = f'https://api.edamam.com/search?q={query}&app_id={api_id}&app_key={api_key}'

    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        print(data)
        recipes = data.get('hits', [])
        with open('recipes.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return recipes
    else:
        return None
