from django.shortcuts import render, redirect
from .models import Users, Favouritemovies
from review_app.models import Reviews
from .forms import UserRegistrationForm

# Create your views here.
def display_users_page(request):
    users = Users.get_users_head()
    reviews = Reviews.get_reviews_head()
    return render(request, 'users.html',
                  {'users': users, 'reviews': reviews})

def display_user_details_page(request, user_id):
    user = Users.get_user(user_id)
    user_favorite_movies = user.get_user_favorite_movies()
    user_reviews = user.get_user_reviews()
    context = {'user': user, 'user_favorite_movies': user_favorite_movies,
               'user_reviews': user_reviews}
    return render(request, 'user_details.html', context=context)

def display_sample_user_details_page(request):
    user = Users.get_user(2)
    user_favorite_movies = user.get_user_favorite_movies()
    user_reviews = user.get_user_reviews()
    context = {'user': user, 'user_favorite_movies': user_favorite_movies,
               'user_reviews': user_reviews}
    return render(request, 'user_details.html', context=context)


def display_login_page(request):
    return render(request, 'login.html')


def display_register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_app:login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context=context)
