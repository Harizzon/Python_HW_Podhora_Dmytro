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
    actors_id integer NOT NULL,
    actor_name character varying(50) NOT NULL,
    age smallint NOT NULL
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    director_id integer NOT NULL,
    director_name character varying(50) NOT NULL,
    age integer NOT NULL,
    number_of_films character varying(100) NOT NULL
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    films_id integer NOT NULL,
    film_name text NOT NULL,
    relese_date integer NOT NULL
);


ALTER TABLE public.films OWNER TO postgres;

--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (actors_id, actor_name, age) FROM stdin;
1	Sir John Vincent Hurt	77
2	Christopher Michael Pratt	40
3	Frances Louise McDormand	62
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.directors (director_id, director_name, age, number_of_films) FROM stdin;
1	James Robert Jarmusch	67	15
2	James Francis Gunn Jr.	53	17
3	Wesley Wales Anderson	50	13
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.films (films_id, film_name, relese_date) FROM stdin;
1	Moonrise Kingdom	2012
2	Guardians of the Galaxy Vol. 2 	2017
3	Only Lovers Left Alive	2014
\.


--
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (actors_id);


--
-- Name: directors directors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_pkey PRIMARY KEY (director_id);


--
-- Name: films films_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_pkey PRIMARY KEY (films_id);


--
-- PostgreSQL database dump complete
--

