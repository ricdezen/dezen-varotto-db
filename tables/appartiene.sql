CREATE TABLE appartiene
(
    genere character varying(20) NOT NULL,
    libro isbn_code NOT NULL,
    CONSTRAINT appartiene_pkey PRIMARY KEY (libro, genere),
    CONSTRAINT appartiene_genere_fkey FOREIGN KEY (genere)
        REFERENCES genere (nome) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT appartiene_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
