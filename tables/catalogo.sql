CREATE TABLE catalogo
(
    fornitore partita_iva NOT NULL,
    libro isbn_code NOT NULL,
    CONSTRAINT catalogo_pkey PRIMARY KEY (fornitore, libro),
    CONSTRAINT catalogo_fornitore_fkey FOREIGN KEY (fornitore)
        REFERENCES fornitore (piva) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT catalogo_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION
)
