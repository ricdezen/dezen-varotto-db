CREATE TABLE appartiene
(
    genere character varying(20) NOT NULL,
    libro codice_isbn NOT NULL,
    CONSTRAINT appartiene_pkey PRIMARY KEY (libro, genere),
    CONSTRAINT appartiene_genere_fkey FOREIGN KEY (genere)
        REFERENCES genere (nome) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT appartiene_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION
)
