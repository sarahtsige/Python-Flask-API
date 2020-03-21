BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE IF NOT EXISTS countries (
    id serial NOT NULL,
    name text NOT NULL,
    region text NOT NULL,
    rank integer NOT NULL,
    happiness_score real NOT NULL,
    CONSTRAINT countries_pkey PRIMARY KEY (id)
);
COPY countries(name, region, rank, happiness_score) FROM '/Users/sarahtsige/sei/projects/Python-Flask-API/happiness/Sheet 1-2015.csv' DELIMITER ',' CSV HEADER;

COMMIT;

ANALYZE countries;
