CREATE TABLE acquisto
(
    numero SERIAL,
    data_acquisto date NOT NULL,
    importo numeric(11,2) NOT NULL,
    dipendente tipo_codice_fiscale NOT NULL,
    CONSTRAINT acquisto_pkey PRIMARY KEY (numero),
    CONSTRAINT acquisto_dipendente_fkey FOREIGN KEY (dipendente)
        REFERENCES dipendente (cf) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT acquisto_importo_positivo CHECK (importo >= 0)
);
