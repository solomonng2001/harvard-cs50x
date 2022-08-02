SELECT name from movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE UPPER(title) LIKE '%TOY STORY%';