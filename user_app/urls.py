from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('', views.display_users_page, name='users'),
    path('details/<int:user_id>/', views.display_user_details_page, name='user_details'),
    path('details/', views.display_sample_user_details_page, name='sample_user_details'),
    path('login/', views.display_login_page, name='login'),
    path('register/', views.display_register_page, name='register'),
]