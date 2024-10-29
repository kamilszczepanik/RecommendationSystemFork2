from django.shortcuts import render
from django.shortcuts import redirect
from .models import Movies, Genredetails, Directorsdetails
from review_app.models import Reviews, Moviecomments






# Create your views here.

def display_movies(request):
    movies_details = Movies.get_movies_head()
    genres = Genredetails.objects.all()  # Pobieranie gatunków
    context = {
        'movies_details': movies_details,
        'genres': genres  # Przekazanie gatunków do szablonu
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
    language = request.selected_language
    if language:
        request.session['language'] = language

    print(f"language: {language}")

    # Pobierz parametry z zapytania GET
    genre = request.GET.get('genre')
    production_year = request.GET.get('production_year')
    director = request.GET.get('director')
    cast = request.GET.get('cast')
    sort_by = request.GET.get('sort_by', 'rating_desc')  # Domyślnie sortowanie po ratingu

    # Pobranie wszystkich dostępnych gatunków i reżyserów do listy rozwijanej
    genres = Genredetails.objects.all()
    directors = Directorsdetails.objects.all()


    # Obsługa różnych opcji sortowania
    if sort_by == 'rating_desc':
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, cast=cast, director=director, sort_by='-rating')
    elif sort_by == 'rating_asc':
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, cast=cast, director=director, sort_by='rating')
    elif sort_by == 'votes_desc':
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, cast=cast, director=director, sort_by='-votes')
    elif sort_by == 'votes_asc':
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, cast=cast, director=director, sort_by='votes')
    else:
        filtered_movies = Movies.sort_movies(genre=genre, production_year=production_year, cast=cast, director=director, sort_by=sort_by)

    # Przekazanie przefiltrowanych filmów, dostępnych gatunków, reżyserów i języka do szablonu
    return render(request, 'movies.html', {
        'movies_details': filtered_movies,
        'genres': genres,
        'directors': directors,
        'language': language  # Przekazujemy język do szablonu
    })




# Funkcja ustawiania języka
def set_language(request):
    language = request.GET.get('language')
    if language:
        request.session['language'] = language
    return redirect(request.META.get('HTTP_REFERER', '/'))