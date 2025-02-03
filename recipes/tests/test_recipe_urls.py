from django.test import TestCase
from django.urls import reverse

class RecipeUrlsTest (TestCase):
    # o nome das dunções tem que começar com teste, não esquecer isso
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'recipe_id': 1})
        self.assertEqual(url, '/recipes/recipe/1/')
