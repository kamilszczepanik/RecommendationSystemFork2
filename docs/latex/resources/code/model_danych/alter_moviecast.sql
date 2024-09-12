ALTER TABLE MovieCast
	ADD CONSTRAINT fk_moviecast_celebrity_id 
		FOREIGN KEY (celebrity_id) 
		REFERENCES MovieCastDetails(celebrity_id),
	ADD CONSTRAINT fk_moviecast_movie_id 
		FOREIGN KEY (movie_id) 
		REFERENCES Movies(movie_id);
