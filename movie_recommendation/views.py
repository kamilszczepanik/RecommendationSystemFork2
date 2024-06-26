from django.shortcuts import render
from movie_app.models import Movies
from review_app.models import Reviews

def homepage(request):
    popular_movies = Movies.get_popular_movies()
    latest_reviews = Reviews.get_latest_review()
    context = {
        'popular_movies': popular_movies,
        'latest_reviews': latest_reviews,
        'range': range(1, 6)  # Dodajemy listę range do kontekstu
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')
