from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.display_user_page),
    path('login/', views.display_login_page),
    path('register/', views.display_register_page),
]