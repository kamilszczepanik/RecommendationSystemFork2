from django.shortcuts import render
from .models import Movies


# Create your views here.

def display_movies(request):
    movies = Movies.get_movies_head()
    return render(request, 'movies.html', {'movies': movies})


def display_film_page(request):
    return render(request, 'movie_details.html')
