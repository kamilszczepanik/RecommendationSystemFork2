ALTER TABLE Reviews
	ADD CONSTRAINT fk_reviews_movie_id 
		FOREIGN KEY (movie_id) 
		REFERENCES Movies(movie_id),
	ADD CONSTRAINT fk_reviews_user_id 
		FOREIGN KEY (user_id) 
		REFERENCES Users(user_id);
