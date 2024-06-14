from django.db import models


# Create your models here.
class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    tittle = models.TextField()
    production_year = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    certificate = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'

    def __str__(self):
        return self.tittle

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


class Directors(models.Model):
    director = models.ForeignKey('Directorsdetails', models.DO_NOTHING)
    movie = models.ForeignKey('Movies', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'directors'


class Directorsdetails(models.Model):
    director_id = models.AutoField(primary_key=True)
    display_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'directorsdetails'


class Genre(models.Model):
    genre = models.ForeignKey('Genredetails', models.DO_NOTHING)
    movie = models.ForeignKey('Movies', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'genre'


class Genredetails(models.Model):
    genre_id = models.AutoField(primary_key=True)
    display_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'genredetails'


class Moviecast(models.Model):
    celebrity = models.ForeignKey('Moviecastdetails', models.DO_NOTHING)
    movie = models.ForeignKey('Movies', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'moviecast'


class Moviecastdetails(models.Model):
    celebrity_id = models.AutoField(primary_key=True)
    display_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'moviecastdetails'
