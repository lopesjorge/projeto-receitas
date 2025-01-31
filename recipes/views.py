from django.shortcuts import get_list_or_404, get_object_or_404, render
from recipes.models import Recipe

def home (request):
    recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', 
        context={
           'recipes': recipes,
        }) 

def category (request, category_id):
#get_list_or_404 retorna uma lista ou 404 - page not found
#Geralemente usado por padrão
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', 
        context={
           'recipes': recipes,
           'title': f'{recipes[0].category.name} - Category | ',
        }) 


def recipe (request, recipe_id):
    #get_list_or_404 retorna o objeto ou 404 - page not found
    recipe = get_object_or_404(Recipe, id=recipe_id, is_published=True) 
    
    return render(request, 'recipes/pages/recipe-view.html', 
        context={
           'recipe': recipe,
           'is_detail_page': True,
        }) #name espace
