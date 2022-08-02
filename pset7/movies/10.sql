SELECT DISTINCT(name) FROM ratings
JOIN movies ON ratings.movie_id = movies.id
JOIN directors ON movies.id = directors.movie_Id
JOIN people ON people.id = directors.person_id
WHERE rating >= 9.0;