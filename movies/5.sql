SELECT title, year FROM movies WHERE UPPER(TRIM(title)) LIKE 'HARRY POTTER%' ORDER BY year;