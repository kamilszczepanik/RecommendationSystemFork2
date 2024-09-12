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