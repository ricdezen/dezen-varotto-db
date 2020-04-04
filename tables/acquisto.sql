CREATE TABLE acquisto
(
    numero SERIAL,
    data_acquisto date NOT NULL,
    importo numeric(11,2) NOT NULL,
    dipendente tipo_codice_fiscale NOT NULL,
    cliente tipo_codice_fiscale,
    prenotazione integer,
    CONSTRAINT acquisto_pkey PRIMARY KEY (numero),
    CONSTRAINT acquisto_dipendente_fkey FOREIGN KEY (dipendente)
        REFERENCES dipendente (cf) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT acquisto_cliente_fkey FOREIGN KEY (cliente)
        REFERENCES cliente (cf) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT acquisto_prenotazione_fkey FOREIGN KEY (prenotazione)
        REFERENCES prenotazione (numero) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT acquisto_importo_positivo CHECK (importo > 0),
    CONSTRAINT acquisto_cliente_se_prenotazione CHECK (prenotazione IS NULL OR cliente IS NOT NULL)
);
