from django.shortcuts import render

from app.util.recipe_util import search_recipe


def index(request):
    return render(request, 'index.html')


def search(request):
    query = request.GET.get('query', '')
    recipes = search_recipe(query)
    return render(request, 'search_results.html', {'recipes': recipes, 'query': query})

