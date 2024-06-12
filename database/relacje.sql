ALTER TABLE genre
ADD CONSTRAINT fk_genre_movie_id FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
ADD CONSTRAINT fk_genre_genre_id FOREIGN KEY (genre_id) REFERENCES genredetails(genre_id);

ALTER TABLE directors
ADD CONSTRAINT fk_directors_movie_id FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
ADD CONSTRAINT fk_directors_director_id FOREIGN KEY (director_id) REFERENCES directorsdetails(celebrity_id);

ALTER TABLE moviecast
ADD CONSTRAINT fk_moviecast_movie_id FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
ADD CONSTRAINT fk_moviecast_celebrity_id FOREIGN KEY (celebrity_id) REFERENCES castdetails(celebrity_id);


ALTER TABLE Reviews
ADD CONSTRAINT fk_reviews_movie_id
FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
ON DELETE CASCADE
ON UPDATE CASCADE;


ALTER TABLE Reviews
ADD CONSTRAINT fk_reviews_user_id
FOREIGN KEY (user_id) REFERENCES Users(user_id)
ON DELETE CASCADE
ON UPDATE CASCADE;


ALTER TABLE MovieComments
ADD CONSTRAINT fk_moviecomments_review_id
FOREIGN KEY (review_id) REFERENCES Reviews(review_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE MovieComments
ADD CONSTRAINT fk_moviecomments_user_id
FOREIGN KEY (user_id) REFERENCES Users(user_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE FavouriteMovies
ADD CONSTRAINT fk_favouritemovies_movie_id
FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

ALTER TABLE FavouriteMovies
ADD CONSTRAINT fk_favouritemovies_user_id
FOREIGN KEY (user_id) REFERENCES Users(user_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

