CREATE TABLE acquisto
(
    numero SERIAL,
    data_acquisto date NOT NULL,
    dipendente codice_fiscale NOT NULL,
    cliente codice_fiscale,
    numero_prenotazione integer,
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
        ON DELETE NO ACTION
    /* + Constraint tale che se numero_prenotazione NOT NULL allora cliente NOT NULL */
)
