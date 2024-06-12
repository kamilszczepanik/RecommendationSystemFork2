from django.db import models


# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    vote_count = models.IntegerField()
    pg_rating = models.CharField(max_length=10)
    duration = models.IntegerField()
    cast = models.ManyToManyField('Cast', related_name='movies')

    def __str__(self):
        return self.title

    def get_cast(self):
        return self.cast.all()

    def get_movie(self, id):
        return self.objects.get(pk=id)

    def get_movies(self):
        return self.objects.all()

    def query_movies(self, name=None, genre=None):
        if name:
            return self.objects.filter(title__icontains=name)
        if genre:
            return self.objects.filter(genre__icontains=genre)
        return self.objects.all()

    def sort_movies(self, name, genre, sort_by='rating'):
        movies = self.query_movies(name=name, genre=genre)
        return movies.order_by(sort_by)


class Cast(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_movies(self):
        return self.movies.all()

    def get_celebrity(self, id):
        return self.objects.get(pk=id)
