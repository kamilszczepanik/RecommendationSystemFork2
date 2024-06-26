from django.shortcuts import render
from movie_app.models import Movies

def homepage(request):
    popular_movies = Movies.get_popular_movies()
    context = {
        'popular_movies': popular_movies
    }
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')
