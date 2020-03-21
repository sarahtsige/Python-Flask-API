BEGIN;

SET client_encoding = 'LATIN1';


CREATE TABLE countries (
    id serial NOT NULL,
    name text NOT NULL,
    region text NOT NULL,
    rank integer NOT NULL,
    happiness_score real NOT NULL,
    CONSTRAINT country_continent_check CHECK ((((((((continent = 'Asia'::text) OR (continent = 'Europe'::text)) OR (continent = 'North America'::text)) OR (continent = 'Africa'::text)) OR (continent = 'Oceania'::text)) OR (continent = 'Antarctica'::text)) OR (continent = 'South America'::text)))
);


COPY countries (code, name, continent, region, surfacearea, indepyear, population, lifeexpectancy, gnp, gnpold, localname, governmentform, headofstate, capital, code2) FROM stdin;




ALTER TABLE ONLY countries
    ADD CONSTRAINT countries_pkey PRIMARY KEY (code);

COMMIT;

ANALYZE countries;
