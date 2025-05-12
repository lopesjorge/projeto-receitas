from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http.response import Http404
from django.db.models import Q
from recipes.models import Recipe
from utils.recipes.pagination import make_pagination
import os
from django.contrib import messages


PER_PAGE = int(os.environ.get('PER_PAGE', 6))

def home (request):
    recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    messages.error(request, 'Epa, você foi pesquisar algo que eu vi.')


    return render(request, 'recipes/pages/home.html', 
        context={
           'recipes': page_obj,
           'pagination_range': pagination_range
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

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/category.html', 
        context={
           'title': f'{recipes[0].category.name} - Category | ',
           'recipes': page_obj,
           'pagination_range': pagination_range,
        }) 


def recipe (request, recipe_id):
    #get_list_or_404 retorna o objeto ou 404 - page not found
    recipe = get_object_or_404(Recipe, id=recipe_id, is_published=True) 
    
    return render(request, 'recipes/pages/recipe-view.html', 
        context={
           'recipe': recipe,
           'is_detail_page': True,
        }) #name espace


def search (request):
    search_term = request.GET.get('q','').strip()

    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains = search_term) | 
            Q(description__icontains = search_term),
        ),

        is_published=True,
    ).order_by('-id')
    
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html',context={
        'page_title':f'Search for: "{search_term}"',
        'search_term':search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })