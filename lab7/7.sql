SELECT AVG(energy) FROM artists
JOIN songs ON artists.id = songs.artist_id
WHERE UPPER(TRIM(artists.name)) = 'DRAKE';