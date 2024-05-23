-- Tworzenie tabeli Movies
CREATE TABLE Movies (
    movie_id SERIAL PRIMARY KEY,
    genre_id INT NOT NULL,
    cast_id INT NOT NULL,
    director_id INT NOT NULL,
    name TEXT NOT NULL,
    year INT NOT NULL,
    rating FLOAT,
    certificate TEXT,
    duration TEXT,
    gross_income INT,
    description TEXT
);

-- Tworzenie tabeli Users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    login TEXT NOT NULL,
    password_hash BYTEA NOT NULL,
    salt BYTEA NOT NULL,
    display_name TEXT NOT NULL,
    role TEXT NOT NULL
);

-- Tworzenie tabeli Reviews
CREATE TABLE Reviews (
    review_id SERIAL PRIMARY KEY,
    movie_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT NOT NULL,
    date DATE NOT NULL,
    content TEXT NOT NULL
);

-- Tworzenie tabeli MovieComments
CREATE TABLE MovieComments (
    comment_id SERIAL PRIMARY KEY,
    review_id INT NOT NULL,
    user_id INT NOT NULL,
    content TEXT NOT NULL
);

-- Tworzenie tabeli FavouriteMovies
CREATE TABLE FavouriteMovies (
    favourite_id SERIAL PRIMARY KEY,
    movie_id INT NOT NULL,
    user_id INT NOT NULL
);

-- Tworzenie tabeli Genre
CREATE TABLE GenreDetails (
    genre_id SERIAL PRIMARY KEY,
    display_name TEXT NOT NULL
);

-- Tworzenie tabeli GenreDetails
CREATE TABLE Genre (
    genre_id INT NOT NULL,
    movie_id INT NOT NULL,
    function TEXT NOT NULL,
    PRIMARY KEY (genre_id, movie_id)
);

-- Tworzenie tabeli MovieCast
CREATE TABLE MovieCast (
    cast_id SERIAL PRIMARY KEY,
    movie_id INT NOT NULL,
    celebrity_id INT NOT NULL,
    function TEXT NOT NULL
);

-- Tworzenie tabeli CastDetails
CREATE TABLE CastDetails (
    celebrity_id SERIAL PRIMARY KEY,
    display_name TEXT NOT NULL
);

-- Tworzenie tabeli Directors
CREATE TABLE Directors (
    director_id SERIAL PRIMARY KEY,
    movie_id INT NOT NULL,
    function TEXT NOT NULL
);

-- Tworzenie tabeli DirectorsDetails
CREATE TABLE DirectorsDetails (
    celebrity_id SERIAL PRIMARY KEY,
    display_name TEXT NOT NULL
);
