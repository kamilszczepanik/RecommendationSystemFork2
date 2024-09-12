CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY,
    movie_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT NOT NULL,
    review_date DATE NOT NULL,
    review_text TEXT
);

