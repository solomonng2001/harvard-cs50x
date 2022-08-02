SELECT DISTINCT(name) FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE movies.id IN (
SELECT movies.id FROM people
JOIN stars ON stars.person_id = people.id
JOIN movies ON movies.id = stars.movie_id
WHERE UPPER(TRIM(name)) = 'KEVIN BACON' AND birth = 1958)
AND NOT UPPER(TRIM(name)) = 'KEVIN BACON';