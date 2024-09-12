ALTER TABLE FavouriteMovies
	ADD CONSTRAINT fk_favouritemovies_movie_id 
		FOREIGN KEY (movie_id) 
		REFERENCES Movies(movie_id),
	ADD CONSTRAINT fk_favouritemovies_user_id 
		FOREIGN KEY (user_id) 
		REFERENCES Users(user_id);