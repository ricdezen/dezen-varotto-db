CREATE TABLE pubblica
(
    editore character varying(50) NOT NULL,
    libro codice_isbn NOT NULL,
    data_pubblicazione date NOT NULL,
    CONSTRAINT pubblica_pkey PRIMARY KEY (editore, libro),
    CONSTRAINT pubblica_editore_fkey FOREIGN KEY (editore)
        REFERENCES editore (nome) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT pubblica_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION
)
