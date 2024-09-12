CREATE TABLE FavouriteMovies (
    favourite_id SERIAL PRIMARY KEY,
    movie_id INT NOT NULL,
    user_id INT NOT NULL
);
