from django.db import models
from user_app.models import Users
from movie_app.models import Movies


# Create your models here.
class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    rating = models.IntegerField()
    review_date = models.DateField()
    review_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'

    def __str__(self):
        return self.movie.title + ' - ' + self.author

    def get_reviews(self):
        return self.objects.all()

    def get_review(self, id):
        return self.objects.get(pk=id)

    def query_reviews(self, movie=None, author=None):
        if movie:
            return self.objects.filter(movie=movie)
        if author:
            return self.objects.filter(author__icontains=author)
        return self.objects.all()

    def sort_reviews(self, movie, author, sort_by='rating'):
        reviews = self.query_reviews(movie=movie, author=author)
        return reviews.order_by(sort_by)


class Moviecomments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    review = models.ForeignKey(Reviews, models.DO_NOTHING)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    comment_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moviecomments'

    def __str__(self):
        return self.review.movie.title + ' - ' + self.user.username

    def get_comments(self):
        return self.objects.all()

    def get_comment(self, id):
        return self.objects.get(pk=id)

    def query_comments(self, review=None, user=None):
        if review:
            return self.objects.filter(review=review)
        if user:
            return self.objects.filter(user=user)
        return self.objects.all()

    def sort_comments(self, review, user):
        comments = self.query_comments(review=review, user=user)
        return comments.order_by('date')
