CREATE TABLE actors
(
	actor_id integer PRIMARY KEY,
	actor_name text NOT NULL,
	age varchar (5) NOT NULL,
	fk_film_id integer REFERENCES films(film_id) NOT NULL
	
)