CREATE TABLE ordine
(
    numero SERIAL,
    data_ordine date NOT NULL,
    quantita smallint NOT NULL,
    importo numeric(11,2) NOT NULL,
    libro tipo_codice_isbn NOT NULL,
    fornitore tipo_partita_iva NOT NULL,
    dipendente tipo_codice_fiscale NOT NULL,
    CONSTRAINT ordine_pkey PRIMARY KEY (numero),
    CONSTRAINT ordine_dipendente_fkey FOREIGN KEY (dipendente)
        REFERENCES dipendente (cf) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT ordine_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT ordine_fornitore_fkey FOREIGN KEY (fornitore)
        REFERENCES fornitore (piva) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT ordine_quantita_positiva CHECK (quantita > 0),
    CONSTRAINT ordine_importo_non_negativo CHECK (importo >= 0)
);