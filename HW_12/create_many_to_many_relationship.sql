CREATE TABLE director_film_actor
(
	film_id int REFERENCES films (film_id),
	director_id int REFERENCES directors (director_id),
	actor_id int REFERENCES actors (actor_id),
	
	CONSTRAINT director_film_actor_pkey PRIMARY KEY (film_id, director_id, actor_id) -- composite key
)