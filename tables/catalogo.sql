CREATE TABLE catalogo
(
    distributore tipo_partita_iva NOT NULL,
    libro tipo_codice_isbn NOT NULL,
    prezzo numeric(11,2) NOT NULL,
    CONSTRAINT catalogo_pkey PRIMARY KEY (distributore, libro),
    CONSTRAINT catalogo_distributore_fkey FOREIGN KEY (distributore)
        REFERENCES distributore (piva) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT catalogo_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
