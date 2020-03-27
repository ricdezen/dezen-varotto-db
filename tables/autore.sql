CREATE TABLE autore
(
    id SERIAL,
    nome character varying(20) NOT NULL,
    cognome character varying(20) NOT NULL,
    data_nascita date,
    CONSTRAINT autore_pkey PRIMARY KEY (id)
);
