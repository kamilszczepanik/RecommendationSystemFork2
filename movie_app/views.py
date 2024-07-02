from django.shortcuts import render
from .models import Movies
from review_app.models import Reviews


# Create your views here.

def display_movies(request):
    popular_movies = Movies.get_popular_movies()
    latest_reviews = Reviews.objects.all().order_by('-review_date')[:5]
    context = {
        'popular_movies': popular_movies,
        'latest_reviews': latest_reviews
    }
    return render(request, 'movies.html', context)

def display_movie_details(request, movie_id):
    movie_details = Movies.get_movie_details(movie_id)
    reviews = Reviews.get_review_for_movie(movie_details['movie'])
    context = {
        'movie_details': movie_details,
        'reviews': reviews
    }
    return render(request, 'movie_details.html', context=context)
def display_sample_movie_details(request):
    movie_details = Movies.get_movie_details(1)
    reviews = Reviews.get_review_for_movie(movie_details['movie'])
    context = {
        'movie_details': movie_details,
        'reviews': reviews
    }
    return render(request, 'movie_details.html', context=context)

