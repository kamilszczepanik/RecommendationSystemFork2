-- WYŚWIETLENIE AKTORÓW
-- SELECT DISTINCT m.tittle, mcd.display_name AS actor_name
-- FROM Movies m
-- JOIN MovieCast mc ON m.movie_id = mc.movie_id
-- JOIN MovieCastDetails mcd ON mc.celebrity_id = mcd.celebrity_id
-- WHERE m.tittle = 'Game of Thrones'; 

-- SELECT DISTINCT m.tittle AS movie_tittle, dd.display_name AS director_name
-- FROM Movies m
-- JOIN Directors d ON m.movie_id = d.movie_id
-- JOIN DirectorsDetails dd ON d.director_id = dd.director_id
-- WHERE m.tittle = 'The Matrix';

-- WYŚWIETLENIE RECENZJI
-- SELECT m.tittle AS movie_title, r.review_text
-- FROM Movies m
-- JOIN Reviews r ON m.movie_id = r.movie_id
-- WHERE m.tittle = 'The Dark Knight'; 

-- Wyświetl filmy reżysera
-- SELECT DISTINCT m.tittle AS movie_title
-- FROM Directors d
-- JOIN DirectorsDetails dd ON d.director_id = dd.director_id
-- JOIN Movies m ON d.movie_id = m.movie_id
-- WHERE dd.display_name = 'Christopher Nolan';

-- Wyswietl filmt aktora
-- SELECT DISTINCT m.tittle AS movie_tittle
-- FROM Movies m
-- JOIN MovieCast mc ON m.movie_id = mc.movie_id
-- JOIN MovieCastDetails mcd ON mc.celebrity_id = mcd.celebrity_id
-- WHERE mcd.display_name = 'Christian Bale';

-- Wyświetl gatunki do filmu
-- SELECT DISTINCT m.tittle AS movie_title, gd.display_name AS genre_name
-- FROM Movies m
-- JOIN Genre g ON m.movie_id = g.movie_id
-- JOIN GenreDetails gd ON g.genre_id = gd.genre_id
-- WHERE m.tittle = 'Game of Thrones';

-- Ocena
--SELECT DISTINCT rating FROM movies WHERE tittle = 'Game of Thrones'

-- Ilosc recenzji
-- SELECT DISTINCT votes FROM movies WHERE tittle = 'Game of Thrones'

-- WYSWIETL FILMY
--SELECT DISTINCT tittle FROM movies
-- Wyswietl aktorów
-- SELECT DISTINCT display_name FROM moviecastdetails
-- Wyswietl gatunki
-- SELECT DISTINCT display_name FROM genredetails
-- Wyswietl reżyserów
-- SELECT DISTINCT display_name FROM directorsdetails

-- Filmy do gatunku
-- SELECT DISTINCT m.tittle AS movie_tittle
-- FROM Movies m
-- JOIN Genre g ON m.movie_id = g.movie_id
-- JOIN GenreDetails gd ON g.genre_id = gd.genre_id
-- WHERE gd.display_name = 'Drama'

--SELECT DISTINCT photo_url FROM movies WHERE title = 'Game of Thrones'




