from django.db import models
from user_app.models import User
from movie_app.models import Movie

# Create your models here.
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

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


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

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