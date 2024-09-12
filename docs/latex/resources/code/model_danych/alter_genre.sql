ALTER TABLE Genre
	ADD CONSTRAINT fk_genre_genre_id 
		FOREIGN KEY (genre_id) 
		REFERENCES GenreDetails(genre_id),
	ADD CONSTRAINT fk_genre_movie_id 
		FOREIGN KEY (movie_id) 
		REFERENCES Movies(movie_id);