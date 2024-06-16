from django.shortcuts import render
from .models import Users, Favouritemovies


# Create your views here.
def display_user_page(request):
    users = Users.get_users_head()
    return render(request, 'user_details.html', {'users': users})


def display_login_page(request):
    return render(request, 'login.html')


def display_register_page(request):
    return render(request, 'register.html')
