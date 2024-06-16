from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_movies),
    path('details/', views.display_film_page),
    path('all/', views.display_movies),
]

# urlpatterns = [
#     path('movies/', views.display_movies),
#     path('movies/<int:id>/', views.display_movie),
#     path('movies/<int:id>/cast/', views.display_cast),
#     path('movies/<int:id>/cast/<int:cast_id>/', views.display_celebrity),
#     path('movies/<int:id>/cast/<int:cast_id>/movies/', views.display_movies_by_cast),
#     path('movies/<int:id>/cast/<int:cast_id>/movies/<int:movie_id>/', views.display_movie_by_cast),
#     path('movies/<int:id>/cast/<int:cast_id>/movies/<int:movie_id>/cast/', views.display_cast_by_movie),
#     path('movies/<int:id>/cast/<int:cast_id>/movies/<int:movie_id>/cast/<int:cast_id>/', views.display_celebrity_by_movie),
#     path('movies/<int:id>/cast/<int:cast_id>/movies/<int:movie_id>/cast/<int:cast_id>/movies/', views.display_movies_by_celebrity),
#     path('movies/<int:id>/cast/<int:cast_id>/movies/<int:movie_id>/cast/<int:cast_id>/movies/<int:movie_id>/', views.display_movie_by_celebrity),
#     path('movies/<int:id>/cast/<int:cast_id>/movies/<int:movie_id>/cast/<int:cast_id>/movies/<int:movie_id>/cast/', views.display_cast_by_celebrity),
#     path('movies/<int:id>/cast/<int:cast_id>/movies/<int:movie_id>/cast/<int:cast_id>/movies/<int:movie_id>/cast/<int:cast_id>/', views.display_celebrity_by_celebrity),
# ]
