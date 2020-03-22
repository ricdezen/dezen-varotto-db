CREATE TABLE include
(
    libro isbn_code NOT NULL,
    acquisto integer NOT NULL,
    quantita smallint NOT NULL,
    CONSTRAINT include_pkey PRIMARY KEY (libro, acquisto),
    CONSTRAINT include_acquisto_fkey FOREIGN KEY (acquisto)
        REFERENCES acquisto (numero) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT include_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT quantita_positiva CHECK (quantita > 0)
)
