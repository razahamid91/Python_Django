from django.shortcuts import render
from django.http import HttpResponse

def recipe_list(request):
    return HttpResponse('List of recipe')

def recipe_detail(request, recipe_id):
    return HttpResponse(f'Detail of recipe #{recipe_id}')

def category_list(request):
    return HttpResponse(f'List of category')

def category_detail(request, category):
    return HttpResponse(f'Detail of category: {category}')