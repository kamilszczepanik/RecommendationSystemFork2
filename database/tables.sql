CREATE TABLE Movies (
    movie_id SERIAL PRIMARY KEY,
    tittle TEXT NOT NULL,
    production_year INT,
    rating FLOAT,
    certificate TEXT,
    duration INT,
    description TEXT,
	votes INT
);

CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY,
    movie_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT NOT NULL,
    review_date DATE NOT NULL,
    review_text TEXT
);

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    login TEXT NOT NULL,
    password_hash BYTEA NOT NULL,
    salt BYTEA NOT NULL,
    display_name TEXT NOT NULL,
    user_role TEXT NOT NULL
);

CREATE TABLE MovieComments (
    comment_id SERIAL PRIMARY KEY,
    review_id INT NOT NULL,
    user_id INT NOT NULL,
	comment_text TEXT 
);

CREATE TABLE FavouriteMovies (
    favourite_id SERIAL PRIMARY KEY,
    movie_id INT NOT NULL,
    user_id INT NOT NULL
);

CREATE TABLE DirectorsDetails (
    director_id SERIAL PRIMARY KEY,
    display_name TEXT NOT NULL
);

CREATE TABLE Directors (
    director_id INT NOT NULL,
    movie_id INT NOT NULL
);

CREATE TABLE MovieCastDetails (
    celebrity_id SERIAL PRIMARY KEY,
    display_name TEXT NOT NULL
);

CREATE TABLE MovieCast (
    celebrity_id INT NOT NULL,
    movie_id INT NOT NULL
);

CREATE TABLE GenreDetails (
    genre_id SERIAL PRIMARY KEY,
    display_name TEXT NOT NULL
);

CREATE TABLE Genre (
    genre_id INT NOT NULL,
    movie_id INT NOT NULL
);

