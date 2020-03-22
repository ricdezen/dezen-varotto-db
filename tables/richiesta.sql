CREATE TABLE richiesta
(
    fornitore partita_iva NOT NULL,
    libro isbn_code NOT NULL,
    prenotazione integer NOT NULL,
    quantita smallint NOT NULL,
    CONSTRAINT richiesta_pkey PRIMARY KEY (prenotazione, libro, fornitore),
    CONSTRAINT richiesta_fornitore_fkey FOREIGN KEY (fornitore)
        REFERENCES fornitore (piva) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT richiesta_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT richiesta_prenotazione_fkey FOREIGN KEY (prenotazione)
        REFERENCES prenotazione (numero) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT quantita_positiva CHECK (quantita > 0)
)
