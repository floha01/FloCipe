import requests


def search_recipe(query):
    api_id = '9422b38e'
    api_key = '22d0363e0ff655a4cc2b14a5c9901e24'
    endpoint = f'https://api.edamam.com/search?q={query}&app_id={api_id}&app_key={api_key}'

    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        recipes = data.get('hits', [])
        return recipes
    else:
        return None
