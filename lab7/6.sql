SELECT songs.name FROM artists
JOIN songs ON artists.id = songs.artist_id
WHERE UPPER(TRIM(artists.name)) = 'POST MALONE';