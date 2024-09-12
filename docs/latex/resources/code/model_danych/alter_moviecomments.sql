ALTER TABLE MovieComments
	ADD CONSTRAINT fk_moviecomments_review_id 
		FOREIGN KEY (review_id) 
		REFERENCES Reviews(review_id),
	ADD CONSTRAINT fk_moviecomments_user_id 
		FOREIGN KEY (user_id) 
		REFERENCES Users(user_id);