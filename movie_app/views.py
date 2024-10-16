from django.shortcuts import render
from .models import Movies, Genredetails
from review_app.models import Reviews, Moviecomments



# Create your views here.

def display_movies(request):
    movies_details = Movies.get_movies_head()
    context = {
        'movies_details': movies_details
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


def movies_list(request):
    # Pobierz parametry z zapytania GET
    genre = request.GET.get('genre')
    production_year = request.GET.get('production_year')
    cast = request.GET.get('cast')
    sort_by = request.GET.get('sort_by', 'rating')  # Domyślnie sortowanie po ratingu

    # Pobranie wszystkich dostępnych gatunków do listy rozwijanej
    genres = Genredetails.objects.all()



    # Filtrowanie lub sortowanie filmów
    filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, cast=cast, sort_by=sort_by)

    # Przekazanie przefiltrowanych filmów i dostępnych gatunków do szablonu
    return render(request, 'movies.html', {
        'movies_details': filtered_movies,
        'genres': genres  # przekazujemy wszystkie dostępne gatunki do formularza
    })
