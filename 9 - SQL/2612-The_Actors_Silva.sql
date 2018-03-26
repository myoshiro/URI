SELECT DISTINCT movies.id, movies.name 
FROM movies, actors, movies_actors, genres 
WHERE 
(movies.id=movies_actors.id_movies) AND
(movies_actors.id_actors=actors.id) AND
(actors.name = 'Marcelo Silva' OR actors.name = 'Miguel Silva') AND
(movies.id_genres = genres.id AND genres.description = 'Action')
