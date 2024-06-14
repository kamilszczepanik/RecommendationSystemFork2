from django.db import models
from movie_app.models import Movies

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    login = models.TextField()
    password_hash = models.BinaryField()
    salt = models.BinaryField()
    display_name = models.TextField()
    user_role = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'

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


class Favouritemovies(models.Model):
    favourite_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    user = models.ForeignKey(Users, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'favouritemovies'