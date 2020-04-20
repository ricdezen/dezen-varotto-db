CREATE TABLE ordine
(
    numero SERIAL,
    data_ordine date NOT NULL,
    quantita smallint NOT NULL,
    importo numeric(11,2) NOT NULL,
    libro tipo_codice_isbn NOT NULL,
    distributore tipo_partita_iva NOT NULL,
    dipendente tipo_codice_fiscale NOT NULL,
    CONSTRAINT ordine_pkey PRIMARY KEY (numero),
    CONSTRAINT ordine_dipendente_fkey FOREIGN KEY (dipendente)
        REFERENCES dipendente (cf) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ordine_libro_fkey FOREIGN KEY (libro)
        REFERENCES libro (isbn) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ordine_distributore_fkey FOREIGN KEY (distributore)
        REFERENCES distributore (piva) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT ordine_quantita_positiva CHECK (quantita > 0),
    CONSTRAINT ordine_importo_non_negativo CHECK (importo >= 0)
);