CREATE TABLE prenotazione
(
    numero SERIAL,
    data_prenotazione date NOT NULL,
    prezzo smallint NOT NULL,
    stato stato_prenotazione NOT NULL,
    nome_cliente codice_fiscale NOT NULL,
    nome_dipendente codice_fiscale NOT NULL,
    CONSTRAINT prenotazione_pkey PRIMARY KEY (numero),
    CONSTRAINT prenotazione_nome_cliente_fkey FOREIGN KEY (nome_cliente)
        REFERENCES cliente (cf) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT prenotazione_nome_dipendente_fkey FOREIGN KEY (nome_dipendente)
        REFERENCES cliente (cf) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    CONSTRAINT prezzo_positivo CHECK (prezzo > 0)
)
