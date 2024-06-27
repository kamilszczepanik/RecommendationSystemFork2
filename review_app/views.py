from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Reviews
from movie_app.models import Movies


def add_review(request, movie_id):
    movie = Movies.get_movie(movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.movie = movie
            new_review.user = request.user
            new_review.save()
            return redirect('movie_app:movie_details', movie_id=movie_id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'movie': movie})
