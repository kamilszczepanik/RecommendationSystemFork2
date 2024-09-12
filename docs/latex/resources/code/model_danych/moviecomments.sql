CREATE TABLE MovieComments (
    comment_id SERIAL PRIMARY KEY,
    review_id INT NOT NULL,
    user_id INT NOT NULL,
    comment_text TEXT
);