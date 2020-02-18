CREATE TABLE autore
(
    id SERIAL,
    nome character varying(20) NOT NULL,
    cognome character varying(20) NOT NULL,
    datadinascita date NOT NULL,
    CONSTRAINT autore_pkey PRIMARY KEY (id)
)
