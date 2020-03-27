CREATE TABLE appartiene
(
    libro tipo_codice_isbn NOT NULL,
    genere character varying(20) NOT NULL,
    CONSTRAINT appartiene_pkey PRIMARY KEY (libro, genere),
    CONSTRAINT appartiene_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT appartiene_genere_fkey FOREIGN KEY (genere)
        REFERENCES genere (nome) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT
)
