ALTER TABLE MovieCast
ADD CONSTRAINT fk_moviecast_celebrity_id FOREIGN KEY (celebrity_id) REFERENCES MovieCastDetails(celebrity_id),
ADD CONSTRAINT fk_moviecast_movie_id FOREIGN KEY (movie_id) REFERENCES Movies(movie_id);

ALTER TABLE Directors
ADD CONSTRAINT fk_directors_director_id FOREIGN KEY (director_id) REFERENCES DirectorsDetails(director_id),
ADD CONSTRAINT fk_directors_movie_id FOREIGN KEY (movie_id) REFERENCES Movies(movie_id);

ALTER TABLE Genre
ADD CONSTRAINT fk_genre_genre_id FOREIGN KEY (genre_id) REFERENCES GenreDetails(genre_id),
ADD CONSTRAINT fk_genre_movie_id FOREIGN KEY (movie_id) REFERENCES Movies(movie_id);

ALTER TABLE Reviews
ADD CONSTRAINT fk_reviews_movie_id FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
ADD CONSTRAINT fk_reviews_user_id FOREIGN KEY (user_id) REFERENCES Users(user_id);

ALTER TABLE MovieComments
ADD CONSTRAINT fk_moviecomments_review_id FOREIGN KEY (review_id) REFERENCES Reviews(review_id),
ADD CONSTRAINT fk_moviecomments_user_id FOREIGN KEY (user_id) REFERENCES Users(user_id);

ALTER TABLE FavouriteMovies
ADD CONSTRAINT fk_favouritemovies_movie_id FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
ADD CONSTRAINT fk_favouritemovies_user_id FOREIGN KEY (user_id) REFERENCES Users(user_id);
