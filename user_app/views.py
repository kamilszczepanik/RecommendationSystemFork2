from django.shortcuts import render


# Create your views here.
def display_user_page(request):
    return render(request, 'user_details.html')


def display_login_page(request):
    return render(request, 'login.html')


def display_register_page(request):
    return render(request, 'register.html')
