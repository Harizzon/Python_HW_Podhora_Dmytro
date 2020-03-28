PGDMP     4    (                x         
   homeworkdb    10.12    10.12     �
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �
           1262    24595 
   homeworkdb    DATABASE     �   CREATE DATABASE homeworkdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Ukrainian_Ukraine.1251' LC_CTYPE = 'Ukrainian_Ukraine.1251';
    DROP DATABASE homeworkdb;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            �
           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12924    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            �
           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    24623    actors    TABLE     �   CREATE TABLE public.actors (
    actors_id integer NOT NULL,
    actor_name character varying(50) NOT NULL,
    age smallint NOT NULL
);
    DROP TABLE public.actors;
       public         postgres    false    3            �            1259    24612 	   directors    TABLE     �   CREATE TABLE public.directors (
    director_id integer NOT NULL,
    director_name character varying(50) NOT NULL,
    age integer NOT NULL,
    number_of_films character varying(100) NOT NULL
);
    DROP TABLE public.directors;
       public         postgres    false    3            �            1259    24604    films    TABLE     |   CREATE TABLE public.films (
    films_id integer NOT NULL,
    film_name text NOT NULL,
    relese_date integer NOT NULL
);
    DROP TABLE public.films;
       public         postgres    false    3            �
          0    24623    actors 
   TABLE DATA               <   COPY public.actors (actors_id, actor_name, age) FROM stdin;
    public       postgres    false    198   �       �
          0    24612 	   directors 
   TABLE DATA               U   COPY public.directors (director_id, director_name, age, number_of_films) FROM stdin;
    public       postgres    false    197          �
          0    24604    films 
   TABLE DATA               A   COPY public.films (films_id, film_name, relese_date) FROM stdin;
    public       postgres    false    196   �       z
           2606    24627    actors actors_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (actors_id);
 <   ALTER TABLE ONLY public.actors DROP CONSTRAINT actors_pkey;
       public         postgres    false    198            x
           2606    24616    directors directors_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.directors
    ADD CONSTRAINT directors_pkey PRIMARY KEY (director_id);
 B   ALTER TABLE ONLY public.directors DROP CONSTRAINT directors_pkey;
       public         postgres    false    197            v
           2606    24611    films films_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.films
    ADD CONSTRAINT films_pkey PRIMARY KEY (films_id);
 :   ALTER TABLE ONLY public.films DROP CONSTRAINT films_pkey;
       public         postgres    false    196            �
   b   x���	�0 �s2E&� ��(�'/��VҸ���+`c�)�@;����B�b	�N��޸�V1�P�X� ����rr��>�m�	M�G��z��      �
   a   x�-ʱ@@ й��~�8�c���h�XMH��u��g0�� ����kf�)&=�-���կ�&Yv�>�P��נ������t|����.�P��8��|�|      �
   c   x�ʱ@0й�+�4��l2��L�&�T_�"����)� �ό��m�C��4dTw��x3dŹ3:��b��a�*5�����)��z���_k�5}�\�     