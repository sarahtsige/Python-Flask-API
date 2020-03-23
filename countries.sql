BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE IF NOT EXISTS country (
    id serial NOT NULL,
    name text NOT NULL,
    region text NOT NULL,
    rank integer NOT NULL,
    happiness_score real NOT NULL,
    CONSTRAINT countries_pkey PRIMARY KEY (id)
);

TRUNCATE TABLE country RESTART IDENTITY;;

COPY country(name, region, rank, happiness_score) FROM '/Users/sarahtsige/sei/projects/Python-Flask-API/happiness/Sheet 1-2015.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE IF NOT EXISTS region (
    id serial NOT NULL,
    name text NOT NULL,
    CONSTRAINT region_pkey PRIMARY KEY (id)
);

TRUNCATE TABLE region RESTART IDENTITY;;

INSERT into region(name)
SELECT DISTINCT region 
FROM country 
WHERE NOT EXISTS (SELECT name FROM region);


ALTER TABLE country
ADD COLUMN IF NOT EXISTS region_id integer;

UPDATE country
SET region_id = region.id
from region 
WHERE country.region = region.name;

COMMIT;

ANALYZE country;

--\i countries.sql