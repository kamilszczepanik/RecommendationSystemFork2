from django.shortcuts import render, redirect
from .models import Users, Favouritemovies
from review_app.models import Reviews
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password


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
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(login=login)
        except Users.DoesNotExist:
            return render(request, 'login.html',
                          {'form': AuthenticationForm(),
                           'error': 'User not found'})
        password_hash = bytes(user.password_hash).decode('utf-8')
        if check_password(password, password_hash):
            request.session['user_id'] = user.user_id
            print('User ID:', request.session['user_id'], 'logged in')
            return redirect('user_app:user_details', user_id=user.user_id)
        else:
            return render(request, 'login.html',
                          {'form': AuthenticationForm(),
                           'error': 'Incorrect password'})
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})


def display_register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('user_app:login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context=context)
