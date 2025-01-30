from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

def home (request):
    recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', 
        context={
           'recipes': recipes,
        }) 

def category (request, category_id):
    #filtrar categoria usar o __ para acessar o campo desejado da foreikey 
    recipes = Recipe.objects.filter(
        category__id = category_id,
        is_published=True,
    )
    
    return render(request, 'recipes/pages/category.html', 
        context={
           'recipes': recipes,
        }) 


def recipe (request, recipe_id):
    #Get pega apenas o objeto por id, nesse caso o id da receita
    recipe = Recipe.objects.get(
        id = recipe_id
    )
    
    return render(request, 'recipes/pages/recipe-view.html', 
        context={
           'recipe': recipe,
           'is_detail_page': True,
        }) #name espace
