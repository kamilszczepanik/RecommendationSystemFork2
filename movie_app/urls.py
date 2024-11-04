from django.urls import path
from . import views

app_name = 'movie_app'

urlpatterns = [
    path('set_language/', views.set_language, name='set_language'),
    path('', views.display_movies, name='display_movies'),
    path('details/<int:movie_id>/', views.display_movie_details, name='movie_details'),
]