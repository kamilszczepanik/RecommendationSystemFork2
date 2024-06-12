from django.db import models
from movie_app.models import Movie

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    favorite_movies = models.ManyToManyField(Movie, related_name='favorited_by')

    def __str__(self):
        return self.username

    def get_user(self, id):
        return self.objects.get(pk=id)

    def get_users(self):
        return self.objects.all()

    def get_user_reviews(self):
        return self.reviews.all()

    def get_user_comments(self):
        return self.comments.all()

    def query_users(self, username=None, email=None):
        if username:
            return self.objects.filter(username__icontains=username)
        if email:
            return self.objects.filter(email__icontains=email)
        return self.objects.all()

    def sort_users(self, username, email, sort_by='date_joined'):
        users = self.query_users(username=username, email=email)
        return users.order_by(sort_by)
