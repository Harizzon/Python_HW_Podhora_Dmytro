--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12
-- Dumped by pg_dump version 10.12

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    actor_id integer NOT NULL,
    actor_name text NOT NULL,
    age character varying(5) NOT NULL,
    fk_film_id integer NOT NULL
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: director_film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.director_film (
    film_id integer NOT NULL,
    director_id integer NOT NULL
);


ALTER TABLE public.director_film OWNER TO postgres;

--
-- Name: director_film_actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.director_film_actor (
    film_id integer NOT NULL,
    director_id integer NOT NULL,
    actor_id integer NOT NULL
);


ALTER TABLE public.director_film_actor OWNER TO postgres;

--
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    director_id integer NOT NULL,
    director_name text NOT NULL,
    age integer NOT NULL,
    fk_film_id integer
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    film_id integer NOT NULL,
    film_name text NOT NULL,
    relese_date character varying(10)
);


ALTER TABLE public.films OWNER TO postgres;

--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (actor_id, actor_name, age, fk_film_id) FROM stdin;
1	Marlon Brando	80	1
2	Alfredo James "Al" 'Pacino	79	1
3	Tim Robbins	61	2
4	Liam Neeson	67	3
5	Robert De Niro	76	4
6	Humphrey Bogart	57	5
7	Orson Welles	70	6
\.


--
-- Data for Name: director_film; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.director_film (film_id, director_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
\.


--
-- Data for Name: director_film_actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.director_film_actor (film_id, director_id, actor_id) FROM stdin;
1	1	1
2	2	2
3	3	3
4	4	4
5	5	5
6	6	6
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.directors (director_id, director_name, age, fk_film_id) FROM stdin;
1	Francis Ford Coppola	80	1
2	Francis Ford Coppola	61	2
3	Steven Spielberg	73	3
4	 Michael Curtiz	73	5
5	 Martin Scorsese	77	4
6	 Orson Welles	70	6
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.films (film_id, film_name, relese_date) FROM stdin;
1	The Godfather	1972
2	The Shawshank Redemption	1994
3	Schindler's List	1993
4	Raging Bull	1980
5	Casablanca	1942
6	Citizen Kane	1941
\.


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (actor_id);


--
-- Name: director_film_actor director_film_actor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director_film_actor
    ADD CONSTRAINT director_film_actor_pkey PRIMARY KEY (film_id, director_id, actor_id);


--
-- Name: director_film director_film_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director_film
    ADD CONSTRAINT director_film_pkey PRIMARY KEY (film_id, director_id);


--
-- Name: directors directors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_pkey PRIMARY KEY (director_id);


--
-- Name: films films_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_pkey PRIMARY KEY (film_id);


--
-- Name: actors actors_fk_film_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_fk_film_id_fkey FOREIGN KEY (fk_film_id) REFERENCES public.films(film_id);


--
-- Name: director_film_actor director_film_actor_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director_film_actor
    ADD CONSTRAINT director_film_actor_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(actor_id);


--
-- Name: director_film_actor director_film_actor_director_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director_film_actor
    ADD CONSTRAINT director_film_actor_director_id_fkey FOREIGN KEY (director_id) REFERENCES public.directors(director_id);


--
-- Name: director_film_actor director_film_actor_film_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director_film_actor
    ADD CONSTRAINT director_film_actor_film_id_fkey FOREIGN KEY (film_id) REFERENCES public.films(film_id);


--
-- Name: director_film director_film_director_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director_film
    ADD CONSTRAINT director_film_director_id_fkey FOREIGN KEY (director_id) REFERENCES public.directors(director_id);


--
-- Name: director_film director_film_film_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director_film
    ADD CONSTRAINT director_film_film_id_fkey FOREIGN KEY (film_id) REFERENCES public.films(film_id);


--
-- Name: directors directors_fk_film_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_fk_film_id_fkey FOREIGN KEY (fk_film_id) REFERENCES public.films(film_id);


--
-- PostgreSQL database dump complete
--

