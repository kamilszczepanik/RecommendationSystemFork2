from django.shortcuts import render
from .models import Movies
from review_app.models import Reviews

# Create your views here.

def display_movies(request):
    movies_details = Movies.get_movies_head()
    print(movies_details[0])
    return render(request, 'movies.html', {'movies_details': movies_details})


def display_film_page(request):
    movie_details = Movies.get_movie_details(1)
    reviews = Reviews.get_review_for_movie(movie_details['movie'])
    context = {
        'movie_details': movie_details,
        'reviews': reviews
    }
    return render(request, 'movie_details.html', context=context)
