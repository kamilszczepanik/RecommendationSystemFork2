from django.db.models import Value

from movie_app.models import Movies, Genredetails
from review_app.models import Reviews
from user_app.models import Users


class MovieRecommender:
    # How many stars are considered a positive review
    rating_threshold: int = 4
    # How many recent reviews/favourites to consider for the algorithm
    __search_limit: int = 3

    def __init__(self, count: int = 30):
        super().__init__()
        self.count = count

    def movie_recommendations(self, movie: Movies) -> Movies:
        """
        Usage:
        some_movie: Movies = ...
        recommended_movies: Movies = MovieRecommender(count=50).movie_recommendations(some_movie)
        """
        smart_recommendations = self.__from_positive_reviews(movie)
        smart_recommendations = smart_recommendations.all().annotate(
            custom_order=Value(1)
        )

        genre_recommendations = self.__popular_in_genres(movie)
        genre_recommendations = genre_recommendations.all().annotate(
            custom_order=Value(2)
        )

        movies = smart_recommendations.union(genre_recommendations).order_by(
            "custom_order", "-rating", "title"
        )[: self.count]
        return movies

    def user_recommendations(self, user: Users) -> Movies:
        """
        Usage:
        some_user: Users = ...
        recommended_movies: Movies = MovieRecommender(count=50).user_recommendations(some_user)
        """
        return self.__from_recent_positive_reviews(user=user)

    def __from_positive_reviews(self, movie: Movies) -> Movies:
        # TODO(@Michał Bugdoł) - order by -date and limit to __search_limit?
        positive_reviews = Reviews.objects.filter(
            movie__in=movie, rating__gte=MovieRecommender.rating_threshold
        )
        recommending_users = positive_reviews.values_list("user", flat=True)
        users_recommend_movies = (
            Reviews.objects.filter(
                user__in=recommending_users,
                rating__gte=MovieRecommender.rating_threshold,
            )
            .exclude(movie__in=movie)
            .values_list("movie", flat=True)
        )
        movies = Movies.objects.filter(movie_id__in=users_recommend_movies).distinct()
        return movies

    def __popular_in_genres(self, movie: Movies) -> Movies:
        genres = Genredetails.objects.filter(genre__movie__in=movie)
        movies = (
            Movies.objects.filter(
                genre__genre__in=genres, rating__gte=MovieRecommender.rating_threshold
            )
            .exclude(movie_id__in=movie.values("movie_id"))
            .distinct()
        )
        return movies

    def __from_recent_positive_reviews(self, user: Users) -> Movies:
        limit_reviews = 10
        recent_reviews = Reviews.objects.filter(
            user=user, rating__gte=MovieRecommender.rating_threshold
        )[:limit_reviews]
        liked_movies = Movies.objects.filter(
            movie_id__in=recent_reviews.values_list("movie", flat=True)
        )

        return self.movie_recommendations(liked_movies)
