from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display_movies(request):
    return HttpResponse(render(request, 'movies.html'))
