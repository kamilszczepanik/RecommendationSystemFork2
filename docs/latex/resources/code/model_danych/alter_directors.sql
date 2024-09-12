ALTER TABLE Directors
	ADD CONSTRAINT fk_directors_director_id 
		FOREIGN KEY (director_id) 
		REFERENCES DirectorsDetails(director_id),
	ADD CONSTRAINT fk_directors_movie_id 
		FOREIGN KEY (movie_id) 
		REFERENCES Movies(movie_id);