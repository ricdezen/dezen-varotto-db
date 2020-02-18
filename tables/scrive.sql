CREATE TABLE scrive
(
    autore integer NOT NULL,
    libro isbn_code NOT NULL,
    CONSTRAINT scrive_autore_fkey FOREIGN KEY (autore)
        REFERENCES autore (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT scrive_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
