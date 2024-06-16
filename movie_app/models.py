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

    @classmethod
    def get_movie(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def get_movies(cls):
        return cls.objects.all()

    @classmethod
    def query_movies(cls, tittle=None, genre=None):
        if tittle:
            return cls.objects.filter(title__icontains=tittle)
        if genre:
            return cls.objects.filter(genre__icontains=genre)
        return cls.objects.all()

    @classmethod
    def sort_movies(cls, tittle, genre, sort_by='rating'):
        movies = cls.query_movies(tittle=tittle, genre=genre)
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
