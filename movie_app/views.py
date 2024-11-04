from django.shortcuts import render
from django.shortcuts import redirect
from .models import Movies, Genredetails, Directorsdetails
from review_app.models import Reviews, Moviecomments
from django.views.decorators.http import require_POST







# Create your views here.


def set_language(request):
    language = request.POST.get('language')
    if language in ['en', 'pl', 'de']:
        request.session['language'] = language
    # Przekierowanie na poprzednią stronę, aby odświeżyć widok
    return redirect(request.META.get('HTTP_REFERER', '/'))

def display_movie_details(request, movie_id):
    movie_details = Movies.get_movie_details(movie_id)
    reviews = Reviews.get_review_for_movie(movie_details['movie'])
    context = {
        'movie_details': movie_details,
        'reviews': reviews
    }
    return render(request, 'movie_details.html', context=context)




def display_movies(request):
    # Pobierz parametry z zapytania GET
    genre = request.GET.get('genre')
    production_year = request.GET.get('production_year')
    director = request.GET.get('director')

    sort_by = request.GET.get('sort_by', 'rating_desc')  # Domyślnie sortowanie po ratingu

    # Pobranie wszystkich dostępnych gatunków i reżyserów do listy rozwijanej
    genres = Genredetails.objects.all()
    directors = Directorsdetails.objects.all()

    # Obsługa różnych opcji sortowania
    if sort_by == 'rating_desc':
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, director=director, sort_by='-rating')
    elif sort_by == 'rating_asc':
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, director=director, sort_by='rating')
    elif sort_by == 'votes_desc':
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, director=director, sort_by='-votes')
    elif sort_by == 'votes_asc':
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, director=director, sort_by='votes')
    else:
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, director=director, sort_by=sort_by)

    # Ograniczenie liczby filmów do 100
    limited_movies = filtered_movies[:100]

    # Przekazanie przefiltrowanych filmów, dostępnych gatunków i reżyserów do szablonu
    return render(request, 'movies.html', {
        'movies_details': limited_movies,
        'genres': genres,
        'directors': directors,
    })


