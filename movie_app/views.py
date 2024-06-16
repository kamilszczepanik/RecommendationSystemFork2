from django.shortcuts import render
from .models import Movies


# Create your views here.

def display_movies(request):
    movies_details = Movies.get_movies_head()
    print(movies_details[0])
    return render(request, 'movies.html', {'movies_details': movies_details})


def display_film_page(request):
    movie_details = Movies.get_movie_details(1)
    return render(request, 'movie_details.html', {'movie_details': movie_details})
