CREATE TABLE scrive
(
    autore integer NOT NULL,
    libro tipo_codice_isbn NOT NULL,
    CONSTRAINT scrive_autore_fkey FOREIGN KEY (autore)
        REFERENCES autore (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT scrive_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
