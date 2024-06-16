from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_users_page),
    path('details/', views.display_user_details_page),
    path('login/', views.display_login_page),
    path('register/', views.display_register_page),
]