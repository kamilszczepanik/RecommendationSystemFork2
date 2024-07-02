from django.shortcuts import render
from movie_app.models import Movies
from review_app.models import Reviews
from movie_recommendation.models import MovieRecommender
from user_app.models import Users

def homepage(request):
    recommended_movies = MovieRecommender().user_recommendations(Users.get_user(request.user.user_id)) if request.user.is_authenticated else []
    popular_movies = Movies.get_popular_movies()
    latest_reviews = Reviews.get_latest_review()
    context = {
        'popular_movies': popular_movies,
        'latest_reviews': latest_reviews,
        'recommended_movies': recommended_movies,
        'range': range(1, 6)
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')


def search_view(request):
    query = request.GET.get('q', '').strip()
    movies = Movies.objects.filter(title__icontains=query) if query else []
    return render(request, 'search_results.html', {'movies': movies})





